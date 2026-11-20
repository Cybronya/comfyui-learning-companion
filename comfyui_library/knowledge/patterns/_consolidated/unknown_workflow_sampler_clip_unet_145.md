---
name: unknown_workflow_sampler_clip_unet_145
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.827875
common_nodes: [CLIPLoader, CLIPTextEncode, ColorMatchToReference, ConditioningZeroOut, Image Comparer (rgthree), LoadImage, ReferenceLatent, SZ_KleinTiledKSampler, SaveImage, Seed (rgthree), SimpleMath+, UNETLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/F.2Klein极限超分增加细节 小图变大图_2062158009069031426.json, 图片生成/图生图/Flux.2-Klein9b极限超分增加细节 模糊变高清_2064348600515256322.json, 图片生成/图生图/Klein-一键修复模糊图像变高清_2061427632968921089.json, 图片生成/图生图/Klein-一键修复模糊图像变高清_2081264986487349249.json, 图片生成/图生图/Klein-图片快速修复-图片高清修复-细节修复-模糊变高清_2063571810217713666.json, 图片生成/图生图/Klein-图片快速修复-图片高清修复-细节修复-模糊变高清_2063948736388227073.json, 图片生成/图生图/修复模糊图像变高清-Klein_2060651278337925121.json, 图片生成/图生图/🐳Klein 图像急速修复 模糊变高清🐳_2059941498447290370.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_145

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/F.2Klein极限超分增加细节 小图变大图_2062158009069031426.json、图片生成/图生图/Flux.2-Klein9b极限超分增加细节 模糊变高清_2064348600515256322.json、图片生成/图生图/Klein-一键修复模糊图像变高清_2061427632968921089.json、图片生成/图生图/Klein-一键修复模糊图像变高清_2081264986487349249.json、图片生成/图生图/Klein-图片快速修复-图片高清修复-细节修复-模糊变高清_2063571810217713666.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatchToReference`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `LoadImage`
- `ReferenceLatent`
- `SZ_KleinTiledKSampler`
- `SaveImage`
- `Seed (rgthree)`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImpactInt` —— 6/8 个有
- `孤海注释` —— 6/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/8 个有
- `PreviewImage` —— 5/8 个有
- `DapaoImageAspectRatioResizeNode` —— 3/8 个有
- `GetNode` —— 3/8 个有
- `SetNode` —— 3/8 个有
- `Int` —— 2/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `Note Plus (mtb)` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | res_2s | - | 8 | 75% |
| 调度器 | bong_tangent | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，8 个样本，一致性 75%
- 调度器 最常用 bong_tangent，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
