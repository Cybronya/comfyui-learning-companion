---
name: unknown_workflow_sampler_clip_unet_344
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.904
common_nodes: [ApplyFBCacheOnModel, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, DualCLIPLoader, EmptySD3LatentImage, Flex2Conditioner, FlexGuidance, ImpactInt, KSampler, LayerUtility: PurgeVRAM, LoadImage, RH_Captioner, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Flex.2+DEEPSEEK图片反推洗图专用工作流_1925012752870350849.json, 图片生成/图生图/Flex.2+LORA图片反推洗图专用工作流_1917435411239735297.json, 图片生成/图生图/Flex.2图片反推洗图工作流_1916314155664740353.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_344

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flex.2+DEEPSEEK图片反推洗图专用工作流_1925012752870350849.json、图片生成/图生图/Flex.2+LORA图片反推洗图专用工作流_1917435411239735297.json、图片生成/图生图/Flex.2图片反推洗图工作流_1916314155664740353.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyFBCacheOnModel`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `Flex2Conditioner`
- `FlexGuidance`
- `ImpactInt`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `RH_Captioner`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GoogleTranslateTextNode` —— 2/3 个有
- `ImageUpscaleWithModel` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `Note Plus (mtb)` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `JWImageResizeByLongerSide` —— 1/3 个有
- `JanusImageUnderstanding` —— 1/3 个有
- `JanusModelLoader` —— 1/3 个有
- `RH_Translator` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | deis | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
