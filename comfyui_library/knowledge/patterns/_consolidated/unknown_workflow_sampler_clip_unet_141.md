---
name: unknown_workflow_sampler_clip_unet_141
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.913875
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoadImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/4o 同款动森风格转绘｜一键生图系列_1908531859959984130.json, 图片生成/图生图/FLUX-一键3D卡通玩偶生成_1916408957932605441.json, 图片生成/图生图/Krea Dev Pulid换脸对比_1950994961493860353.json, 图片生成/图生图/PVC 玩偶手办｜一键生图系列_1909914716737863682.json, 图片生成/图生图/任何 人物角色  3D 形象 转换｜一键生图系列_1908028995135221762.json, 图片生成/图生图/全能图片G-4o_真人转3D头像_1911383209878220801.json, 图片生成/图生图/全能图片G4o 同款 JOJO 风｜一键生图系列_1909501337153712129.json, 图片生成/图生图/全能图片G4o 同款史努比卡通风格｜一键生图系列_1908447812558987266.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_141

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/4o 同款动森风格转绘｜一键生图系列_1908531859959984130.json、图片生成/图生图/FLUX-一键3D卡通玩偶生成_1916408957932605441.json、图片生成/图生图/Krea Dev Pulid换脸对比_1950994961493860353.json、图片生成/图生图/PVC 玩偶手办｜一键生图系列_1909914716737863682.json、图片生成/图生图/任何 人物角色  3D 形象 转换｜一键生图系列_1908028995135221762.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/8 个有
- `ConcatTextOfUtils` —— 5/8 个有
- `EmptyLatentImage` —— 5/8 个有
- `LoraLoader` —— 5/8 个有
- `VAEEncode` —— 5/8 个有
- `EmptySD3LatentImage` —— 3/8 个有
- `SDVN Joy Caption` —— 3/8 个有
- `Joy_caption` —— 2/8 个有
- `Joy_caption_load` —— 2/8 个有
- `Lora Loader Stack (rgthree)` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `easy clearCacheAll` —— 2/8 个有
- `ImageConcatMulti` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有
- `PulidFluxFaceDetector` —— 1/8 个有
- `PulidFluxOptions` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 768 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| LoRA 模型强度 | 0.8 | 0.8 - 1 | 5 | 90% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 768，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 1，5 个样本，取值集中（一致性 90%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
