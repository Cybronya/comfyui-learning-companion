---
name: image_to_image_lora_sampler_unet_86
type: Image To Image
frequency: 7
level: strong
coverage: 0.842714
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2511人物替换--laoxuaistudio_2034861743909904386.json, 图片生成/图生图/2511人物替换-电商不换产品_2044607174063693825.json, 图片生成/图生图/AnyPose + Qwen Image Edit：无需OpenPose，一键让你的动漫IP模仿任意姿势！_2006931333016195074.json, 图片生成/图生图/Anypose_控制人体姿势_2511_2012451454107262978.json, 图片生成/图生图/Anypose_控制人体姿势_2511_2097865491955150849.json, 图片生成/图生图/Anypose_控制人体姿势_2511_2099405588315852802.json, 图片生成/图生图/FireRed-image-edit小红书图像编辑器-视觉领主：定格开源图像编辑的巅峰时刻_2029745829321379842.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_86

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/2511人物替换--laoxuaistudio_2034861743909904386.json、图片生成/图生图/2511人物替换-电商不换产品_2044607174063693825.json、图片生成/图生图/AnyPose + Qwen Image Edit：无需OpenPose，一键让你的动漫IP模仿任意姿势！_2006931333016195074.json、图片生成/图生图/Anypose_控制人体姿势_2511_2012451454107262978.json、图片生成/图生图/Anypose_控制人体姿势_2511_2097865491955150849.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 6/7 个有
- `ConditioningZeroOut` —— 5/7 个有
- `ModelSamplingAuraFlow` —— 5/7 个有
- `FluxKontextImageScale` —— 4/7 个有
- `LayerUtility: ImageReel` —— 4/7 个有
- `LayerUtility: ImageReelComposit` —— 4/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `AIO_Preprocessor` —— 2/7 个有
- `RHHiddenNodes` —— 2/7 个有
- `easy seed` —— 2/7 个有
- `JjkText` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `RH_LLMAPI_NODE` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 7 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（11/7 个样本）：Steps较低可能导致细节不足
