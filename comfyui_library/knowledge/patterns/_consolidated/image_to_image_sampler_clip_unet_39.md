---
name: image_to_image_sampler_clip_unet_39
type: Image To Image
frequency: 9
level: strong
coverage: 0.948778
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/版画艺术生成器_1996222237315309569.json, 图片生成/图生图/电商产品溶图_2026942543119785985.json, 图片生成/图生图/老照片修复flux_kontext全自动修复_2095321572251881474.json, 图片生成/图生图/老照片修复flux_kontext全自动修复_2095425023170400258.json, 图片生成/图生图/老照片修复工作流_1974678865857613826.json, 图片生成/图生图/老照片修复（flux kontext全自动修复）_1990974918315679745.json, 图片生成/图生图/老照片修复（flux kontext全自动修复））_2017623484586790914.json, 图片生成/图生图/课件20：kontext老照片一键修复_2099656538049826818.json, 图片生成/文生图/KontextDev转绘赛璐珞日漫风_1938493107786964994.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_39

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/版画艺术生成器_1996222237315309569.json、图片生成/图生图/电商产品溶图_2026942543119785985.json、图片生成/图生图/老照片修复flux_kontext全自动修复_2095321572251881474.json、图片生成/图生图/老照片修复flux_kontext全自动修复_2095425023170400258.json、图片生成/图生图/老照片修复工作流_1974678865857613826.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 8/9 个有
- `LoraLoaderModelOnly` —— 8/9 个有
- `Image Comparer (rgthree)` —— 6/9 个有
- `RepeatLatentBatch` —— 6/9 个有
- `RH_Translator` —— 4/9 个有
- `ImageResize+` —— 1/9 个有
- `PrimitiveFloat` —— 1/9 个有
- `ttN concat` —— 1/9 个有
- `ttN text` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 9 | 85% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，9 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
