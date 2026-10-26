---
name: unknown_workflow_video_lora_clip_6
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.424875
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, DiffusionModelLoaderKJ, ImageResizeKJv2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, PrimitiveInt, SAM3_VideoTrack, SCAIL2ColoredMask, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/Scail2_v01_2096895345262424066.json, 数字人/数字人/Scail2多参工作流_2096877747174989825.json, 数字人/数字人/一键复刻爆款视频_2097251150608297986.json, 视频生成/图生视频/SCAIL2 动作迁移_角色替换 加强循环流_2073324810372993026.json, 视频生成/图生视频/Scail2_多参_无劣化_2098259674410868737.json, 视频生成/图生视频/Scail2动作迁移_for循环（一键模仿）_2089320207121731586.json, 视频生成/图生视频/Scail2多参工作流_2090458654913941506.json, 视频生成/图生视频/Scail2多参工作流_2093511775273705474.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_6

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/Scail2_v01_2096895345262424066.json、数字人/数字人/Scail2多参工作流_2096877747174989825.json、数字人/数字人/一键复刻爆款视频_2097251150608297986.json、视频生成/图生视频/SCAIL2 动作迁移_角色替换 加强循环流_2073324810372993026.json、视频生成/图生视频/Scail2_多参_无劣化_2098259674410868737.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：42%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DiffusionModelLoaderKJ`
- `ImageResizeKJv2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `PrimitiveInt`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 7/8 个有
- `ComfyMathExpression` —— 7/8 个有
- `Fast Groups Bypasser (rgthree)` —— 7/8 个有
- `GetImageRangeFromBatch` —— 7/8 个有
- `ImageConcatMulti` —— 7/8 个有
- `KSamplerSelect` —— 7/8 个有
- `SamplerCustom` —— 7/8 个有
- `SingleBooleanTrigger` —— 7/8 个有
- `easy batchAnything` —— 7/8 个有
- `easy forLoopEnd` —— 7/8 个有
- `easy forLoopStart` —— 7/8 个有
- `easy imageRemBg` —— 7/8 个有
- `ComfySwitchNode` —— 5/8 个有
- `Float` —— 5/8 个有
- `ImageBatchMultiple+` —— 5/8 个有
- `ImageFromBatch` —— 5/8 个有
- `Label (rgthree)` —— 5/8 个有
- `Int` —— 2/8 个有
- `SaveVideoRGBA` —— 2/8 个有
- `BatchImagesNode` —— 1/8 个有
- `KSampler` —— 1/8 个有
- `PrimitiveBoolean` —— 1/8 个有
- `PrimitiveString` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `WanContextWindowsManual` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | dpmpp_2m_sde_gpu | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
