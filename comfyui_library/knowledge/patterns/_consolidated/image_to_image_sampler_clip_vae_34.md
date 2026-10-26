---
name: image_to_image_sampler_clip_vae_34
type: Image To Image
frequency: 5
level: strong
coverage: 0.7456
common_nodes: [CLIPTextEncode, CR Text, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Kontext Dev三图模式+LLM大模型提示词（效果更加精准）_1938673311859531778.json, 图片生成/图生图/Kontext Dev单图模式+LLM大模型提示词（效果更加精准）_1938492395124097025.json, 图片生成/图生图/Kontext Dev双图模式+LLM大模型提示词（效果更加精准）_1938657364100702210.json, 图片生成/图生图/Kontext nunchaku单图编辑_1939391998157627394.json, 图片生成/图生图/Kontext一键印花、图案提取_1955819052124946433.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_34

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Kontext Dev三图模式+LLM大模型提示词（效果更加精准）_1938673311859531778.json、图片生成/图生图/Kontext Dev单图模式+LLM大模型提示词（效果更加精准）_1938492395124097025.json、图片生成/图生图/Kontext Dev双图模式+LLM大模型提示词（效果更加精准）_1938657364100702210.json、图片生成/图生图/Kontext nunchaku单图编辑_1939391998157627394.json、图片生成/图生图/Kontext一键印花、图案提取_1955819052124946433.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RH_LLMAPI_NODE` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `EmptySD3LatentImage` —— 3/5 个有
- `ImageConcanate` —— 3/5 个有
- `ImageStitch` —— 2/5 个有
- `ImpactInt` —— 2/5 个有
- `easy imageScaleDownToSize` —— 2/5 个有
- `GetNode` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `ModelSamplingFlux` —— 1/5 个有
- `NunchakuFluxDiTLoader` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `StringFunction|pysssss` —— 1/5 个有
- `easy imageSize` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
