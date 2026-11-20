---
name: unknown_workflow_controlnet_lora_sampler_21
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.827667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Text Concatenate, ControlNetApplySD3, ControlNetLoader, DualCLIPLoader, EmptySD3LatentImage, Fast Groups Muter (rgthree), FluxGuidance, ImageResize+, ImageResizeKJ, KSamplerSelect, LoadImage, LoraLoader, PortraitMasterBaseCharacter, RandomNoise, SamplerCustomAdvanced, SaveImage, Seed (rgthree), ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, easy positive]
problems: []
missing: []
members: [图片生成/反推提示词/【人物多角度视图】 Openpose人物不同视图风格一致 (1)_1900813971409248258.json, 图片生成/反推提示词/反推+姿势图生成多视图-角色一致性_1936247756187144193.json, 平台全量/反推提示词生成多视图_1851959086433951746.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_21

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/【人物多角度视图】 Openpose人物不同视图风格一致 (1)_1900813971409248258.json、图片生成/反推提示词/反推+姿势图生成多视图-角色一致性_1936247756187144193.json、平台全量/反推提示词生成多视图_1851959086433951746.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `Fast Groups Muter (rgthree)`
- `FluxGuidance`
- `ImageResize+`
- `ImageResizeKJ`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `PortraitMasterBaseCharacter`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `ReActorRestoreFace` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `ETN_Translate` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `OpenposePreprocessor` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.6 | 0.6 - 0.6 | 3 | 100% |
| LoRA 模型强度 | 0.45 | 0.45 - 0.8 | 3 | 71% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.6，观测区间 0.6 - 0.6，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.45，观测区间 0.45 - 0.8，3 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
