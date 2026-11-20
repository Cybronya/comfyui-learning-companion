---
name: image_to_image_sampler_clip_unet_12
type: Image To Image
frequency: 15
level: strong
coverage: 0.9486
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/dou音斑驳光影特效_1955605349857312769.json, 图片生成/图生图/flux kontext动漫转真人、3D立体_1942222658639441922.json, 图片生成/图生图/flux kontext图像转素描风格_1942221766645452802.json, 图片生成/图生图/flux kontext毛坯转效果图_1946906636578353153.json, 图片生成/图生图/flux1_kontext局部重绘，修改背景_2087011874389970946.json, 图片生成/图生图/kontext_全能溶图打光_1987723006002794498.json, 图片生成/图生图/kontext_全能精修丨产品精修_1947203500150300673.json, 图片生成/图生图/kontext人像草图处理v2_2058796047136288769.json, 图片生成/图生图/一年前的老照片修复技术_1942854549231349761.json, 图片生成/图生图/图片转夜景_1955593052024967169.json, 图片生成/图生图/已知最强老照片修复 高清上色修复 精准还原_2011432965464662017.json, 图片生成/图生图/老照片修复(全能)_2041505459147902978.json, 图片生成/图生图/老照片修复_1992160042147270657.json, 图片生成/图生图/老照片修复_Kontext-DEV开源ComfyUI官方版_1938389131972247553.json, 图片生成/文生图/老照片修复(实用)_1942547476778037249.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_12

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/dou音斑驳光影特效_1955605349857312769.json、图片生成/图生图/flux kontext动漫转真人、3D立体_1942222658639441922.json、图片生成/图生图/flux kontext图像转素描风格_1942221766645452802.json、图片生成/图生图/flux kontext毛坯转效果图_1946906636578353153.json、图片生成/图生图/flux1_kontext局部重绘，修改背景_2087011874389970946.json…）

- **类型**：Image To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 14/15 个有
- `LoraLoaderModelOnly` —— 13/15 个有
- `FluxKontextImageScale` —— 12/15 个有
- `Text Multiline` —— 9/15 个有
- `ShowText|pysssss` —— 7/15 个有
- `ImageConcatMulti` —— 6/15 个有
- `GoogleTranslateTextNode` —— 5/15 个有
- `ImageStitch` —— 5/15 个有
- `Image Comparer (rgthree)` —— 4/15 个有
- `PreviewImage` —— 4/15 个有
- `RepeatLatentBatch` —— 4/15 个有
- `DetailTransfer` —— 2/15 个有
- `GetImageSize+` —— 2/15 个有
- `ImageScale` —— 2/15 个有
- `CompressImages` —— 1/15 个有
- `LoadLatentEXR` —— 1/15 个有
- `LoaderGGUF` —— 1/15 个有
- `SaveLatent` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 12 - 30 | 15 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | simple | - | 15 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 12 - 30，15 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 simple，15 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
