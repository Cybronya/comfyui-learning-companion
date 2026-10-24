---
name: image_to_image_sampler_clip_unet_66
type: Image To Image
frequency: 7
level: strong
coverage: 0.969857
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/dou音斑驳光影特效_1955605349857312769.json, 图片生成/图生图/flux kontext动漫转真人、3D立体_1942222658639441922.json, 图片生成/图生图/flux kontext图像转素描风格_1942221766645452802.json, 图片生成/图生图/flux kontext毛坯转效果图_1946906636578353153.json, 图片生成/图生图/flux1_kontext局部重绘，修改背景_2087011874389970946.json, 图片生成/图生图/flux_kontext 脸部去油，去AI感，真实皮肤_1946634107703947266.json, 图片生成/图生图/图片转夜景_1955593052024967169.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_66

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/dou音斑驳光影特效_1955605349857312769.json、图片生成/图生图/flux kontext动漫转真人、3D立体_1942222658639441922.json、图片生成/图生图/flux kontext图像转素描风格_1942221766645452802.json、图片生成/图生图/flux kontext毛坯转效果图_1946906636578353153.json、图片生成/图生图/flux1_kontext局部重绘，修改背景_2087011874389970946.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/7 个有
- `FluxKontextImageScale` —— 5/7 个有
- `Image Comparer (rgthree)` —— 3/7 个有
- `DetailTransfer` —— 2/7 个有
- `GetImageSize+` —— 2/7 个有
- `ImageScale` —— 2/7 个有
- `Text Multiline` —— 2/7 个有
- `LayerUtility: ImageReel` —— 1/7 个有
- `LayerUtility: ImageReelComposit` —— 1/7 个有
- `LoadLatentEXR` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `SaveLatent` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 12 - 20 | 7 | 85% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 12 - 20，7 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
