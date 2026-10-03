# 工作流分析规则（analysis_rules）

本文件是分析 ComfyUI workflow 的方法论。输出格式见同目录 `workflow_template.md`。

## 1. 先判别输入格式

ComfyUI 有两种 JSON，分析方式不同：

| 特征 | UI 格式（画布保存） | API 格式（Save API 版） |
|---|---|---|
| 顶层键 | `nodes`, `links`, `groups`, `version` | 以数字字符串为键的字典 |
| 连接 | 集中在 `links` 数组 | 内嵌在 inputs 值 `["节点id", 输出槽序号]` |
| 参数 | `widgets_values` 数组 | inputs 里直接是值 |

- UI 格式：`"nodes" in data and isinstance(data.get("nodes"), list)`
- API 格式：顶层键几乎都是数字字符串，且有 `class_type`

解析优先用 `tools/workflow_parser.py`，它会自动判别并归一化输出。

## 2. 分析步骤（固定顺序）

1. **格式判别**：UI / API，节点总数、有无 groups / subgraph。
2. **节点清单**：id、class_type、title（自定义名）、所属插件（内置 or custom_nodes，查 MiniMax H3 项目仓库的 `comfyui/custom_nodes/NODES_SOURCES.md`）。
3. **数据流重建**：从 link type 入手，见下节；从"输出节点"（SaveImage / VHS_VideoCombine / PreviewImage 等）**反向**追溯到输入节点。
4. **模式识别**：对照第 4 节常见模式表，判断这是哪类工作流。
5. **关键参数**：采样器（steps/cfg/denoise/sampler/scheduler/seed）、分辨率与帧数、模型加载（ckpt/unet/lora/vae）、ControlNet 强度等。
6. **资源与显存链路**：模型加载节点类型（是否 MultiGPU 版加载器、fp8/quant 化）、tiled decode 等显存优化痕迹。
7. **可优化点**：冗余节点、可 tiled、可 batch、可加缓存/复用的部分（只提建议，不武断）。

## 3. Link Type 语义（数据流速查）

| 类型 | 含义 | 典型起点 → 终点 |
|---|---|---|
| MODEL | 扩散模型 | CheckpointLoader / UNETLoader → KSampler |
| CLIP | 文本编码器 | CheckpointLoader / CLIPLoader → CLIPTextEncode |
| VAE | 编解码器 | → VAEEncode / VAEDecode |
| LATENT | 潜空间 | EmptyLatentImage / VAEEncode / Sampler → VAEDecode |
| IMAGE | 像素图 | LoadImage → VAEEncode / SaveImage |
| CONDITIONING | 条件（正/负） | CLIPTextEncode → KSampler |
| CONTROL_NET | ControlNet 模型 | ControlNetLoader → ControlNetApply |
| UPSCALE_MODEL | 放大模型 | UpscaleModelLoader → ImageUpscaleWithModel |
| VIDEO / AUDIO | 视频与音频（视频流场景） | VHS / Wan / H3 相关节点 |

> 本项目是视频生成场景：见到 LATENT 带时间维、帧数(FPS/length)参数、
> `Wan` / `MiniMax` / `H3` / `VHS` 字样的节点，按视频链路分析。

## 4. 常见模式识别表

| 模式 | 特征节点组合 |
|---|---|
| 文生图 (t2i) | LoadCheckpoint → CLIPTextEncode×2 → EmptyLatentImage → KSampler → VAEDecode → SaveImage |
| 图生图 (i2i) | 同上，但 EmptyLatentImage 换成 LoadImage + VAEEncode，denoise < 1 |
| 局部重绘 (inpaint) | LoadImage + INPAINT 相关 / SetLatentNoiseMask + VAEEncodeForInpaint |
| ControlNet 控制 | ControlNetLoader + ControlNetApply(Advanced)，Advanced 版 positive/negative 双出 |
| LoRA 叠加 | LoraLoader（可串多个）插在 checkpoint 与 CLIPTextEncode 之间 |
| 放大链路 | UpscaleModelLoader / ImageUpscaleWithModel，或 latent 上行 UpscaleLatent，常接二段 KSampler |
| 视频生成 (Wan 系) | WanImageToVideo / EmptyHunyuanLatentVideo / WanFunControlToVideo 等 + CLIPVisionLoader |
| 视频生成 (H3/MiniMax) | 项目 custom_nodes 中的 MiniMax/H3 相关节点，参考 NODES_SOURCES.md |
| MultiGPU / 卸载 | 项目内 MultiGPU、FastLoad 类节点（见 NODES_SOURCES.md），表现是普通加载器的"高仿版" |
| 帧插值/后处理 | RIFE VFI、VHS_VideoCombine 等视频后端 |

## 5. 输出要求

- 报告语言默认中文，节点名/参数保留英文原词。
- 数据流用文字箭头或 mermaid `flowchart`，从加载器画到输出节点。
- 每个结论都要有依据（引用具体节点 id 或参数值），不猜。
- 分析结束后把索引写入 `memory/workflow_index.json`（字段见该文件内注释）。
- 发现 knowledge/ 未覆盖的节点或概念 → 新建知识卡 + 记入 `learning_records.md`。

## 6. 术语规范

- `denoise`=降噪强度（1.0 全新采样，越低越贴原图）；`cfg`=引导系数；`steps`=采样步数。
- "正/负条件" 指 positive / negative conditioning。
- 视频术语统一：帧数(frames)、帧率(fps)、时长 = frames / fps。
