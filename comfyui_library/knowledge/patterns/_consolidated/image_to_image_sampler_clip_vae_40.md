---
name: image_to_image_sampler_clip_vae_40
type: Image To Image
frequency: 6
level: strong
coverage: 0.9675
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/黑白老照片修复_1982045345473544194.json, 平台全量/Kontext去水印_1972812706128547841.json, 平台全量/Kontext超级快速去水印_1939603880483201026.json, 平台全量/flux-kontext扩图_1962128549937397762.json, 平台全量/无痕扩图 图像边界外扩 图像万能 扩图 真正的无痕扩图_2008338188837851137.json, 平台全量/老照片修复终极版_kontext dev 全面优化加速持续更新_1939755004360364034.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_40

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/黑白老照片修复_1982045345473544194.json、平台全量/Kontext去水印_1972812706128547841.json、平台全量/Kontext超级快速去水印_1939603880483201026.json、平台全量/flux-kontext扩图_1962128549937397762.json、平台全量/无痕扩图 图像边界外扩 图像万能 扩图 真正的无痕扩图_2008338188837851137.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 5/6 个有
- `ConditioningZeroOut` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `NunchakuFluxDiTLoader` —— 4/6 个有
- `UnetLoaderGGUF` —— 4/6 个有
- `ImagePadKJ` —— 2/6 个有
- `LayerUtility: SaveImagePlus` —— 2/6 个有
- `TeaCache` —— 2/6 个有
- `UNETLoader` —— 2/6 个有
- `AddLabel` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有
- `JWImageResizeByLongerSide` —— 1/6 个有
- `LayerUtility: TextBox` —— 1/6 个有
- `NunchakuFluxLoraLoader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 6 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
