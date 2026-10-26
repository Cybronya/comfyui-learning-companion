---
name: unknown_workflow_lora_sampler_clip_85
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.8795
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CheckpointLoaderSimple, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Lora+提示词=风格化图片_1952911676233478146.json, 图片生成/文生图/像素风格插画_1912796321265217537.json, 图片生成/文生图/泡泡液态金属字体_2047922074966036481.json, 图片生成/文生图/游戏道具工具箱工作流_1992976015037235201.json, 图片生成/文生图/美食类游戏蛋糕_1866768530052988929.json, 图片生成/文生图/黏土风icon_1955200823770976258.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_85

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Lora+提示词=风格化图片_1952911676233478146.json、图片生成/文生图/像素风格插画_1912796321265217537.json、图片生成/文生图/泡泡液态金属字体_2047922074966036481.json、图片生成/文生图/游戏道具工具箱工作流_1992976015037235201.json、图片生成/文生图/美食类游戏蛋糕_1866768530052988929.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxResolutionNode` —— 5/6 个有
- `JjkText` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `TextCombinerTwo` —— 5/6 个有
- `Label (rgthree)` —— 3/6 个有
- `DeepTranslatorTextNode` —— 2/6 个有
- `CR String To Combo` —— 1/6 个有
- `Primitive string [Crystools]` —— 1/6 个有
- `Text Multiline` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1024 | 6 | 90% |
| 高度 | 1280 | 1024 - 1536 | 6 | 88% |
| LoRA 模型强度 | 1 | 0.45 - 1.2 | 6 | 75% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1024，6 个样本，取值集中（一致性 90%）
- 高度 中位数 1280，观测区间 1024 - 1536，6 个样本，取值集中（一致性 88%）
- LoRA 模型强度 中位数 1，观测区间 0.45 - 1.2，6 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
