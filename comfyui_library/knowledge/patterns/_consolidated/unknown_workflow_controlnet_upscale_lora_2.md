---
name: unknown_workflow_controlnet_upscale_lora_2
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.291
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApply, ControlNetLoader, Fast Groups Bypasser (rgthree), Florence2ModelLoader, Florence2Run, GetNode, Image Comparer (rgthree), LoadImage, LoraLoader, PreviewImage, SaveImage, SetNode, UltimateSDUpscale, UpscaleModelLoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/SD 图像放大+真实皮肤_1921081166919827457.json, 图片生成/图生图/【人像修图】｜ 图像放大 + 真实皮肤_2000836618774773761.json, 图片生成/图生图/人像修图_2076040416729853953.json, 图片生成/图生图/大厂美图商用人像修图_1925022207250997249.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_lora_2

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/SD 图像放大+真实皮肤_1921081166919827457.json、图片生成/图生图/【人像修图】｜ 图像放大 + 真实皮肤_2000836618774773761.json、图片生成/图生图/人像修图_2076040416729853953.json、图片生成/图生图/大厂美图商用人像修图_1925022207250997249.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：29%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApply`
- `ControlNetLoader`
- `Fast Groups Bypasser (rgthree)`
- `Florence2ModelLoader`
- `Florence2Run`
- `GetNode`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 0.7 | 0.7 - 0.8 | 4 | 94% |
| LoRA 文本强度 | 0 | 0 - 0 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.7，观测区间 0.7 - 0.8，4 个样本，取值集中（一致性 94%）
- LoRA 文本强度 中位数 0，观测区间 0 - 0，4 个样本，取值集中（一致性 100%）
