---
name: unknown_workflow_lora_sampler_clip_134
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.85875
common_nodes: [CLIPTextEncode, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, DualCLIPLoader, Florence2ModelLoader, Florence2Run, FluxGuidance, FluxResolutionNode, HfImageToRGB, ImageBlend, ImageResize+, ImageResizeKJ, InstructPixToPixConditioning, KSampler, LoadImage, LoraLoaderModelOnly, MaskToSEGS, MiDaS-DepthMapPreprocessor, PreviewImage, SEGSPreview, SaveImage, TextCombinerTwo, VAEDecode, easy imageRemBg]
problems: []
missing: []
members: [图片生成/图生图/【最新】史努比 Snoopy 漫画风格_1912885985607385090.json, 图片生成/图生图/一秒走进Snoopy史努比漫画_1908452854783483906.json, 图片生成/图生图/一键把图片改成动漫头像工作流_1890976119351316482.json, 图片生成/文生图/一键生成史努比动漫style_1893202623359823873.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_134

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/【最新】史努比 Snoopy 漫画风格_1912885985607385090.json、图片生成/图生图/一秒走进Snoopy史努比漫画_1908452854783483906.json、图片生成/图生图/一键把图片改成动漫头像工作流_1890976119351316482.json、图片生成/文生图/一键生成史努比动漫style_1893202623359823873.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `DualCLIPLoader`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `FluxResolutionNode`
- `HfImageToRGB`
- `ImageBlend`
- `ImageResize+`
- `ImageResizeKJ`
- `InstructPixToPixConditioning`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToSEGS`
- `MiDaS-DepthMapPreprocessor`
- `PreviewImage`
- `SEGSPreview`
- `SaveImage`
- `TextCombinerTwo`
- `VAEDecode`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `RH_Captioner` —— 3/4 个有
- `TextInput_` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `VAELoader` —— 3/4 个有
- `ControlNetApplyAdvanced` —— 2/4 个有
- `ControlNetLoader` —— 2/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `workflow/clip` —— 1/4 个有
- `workflow/cn` —— 1/4 个有
- `workflow/模型` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| ControlNet 权重 | 0.42 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.42，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
