---
name: image_to_image_sampler_unet_vae_30
type: Image To Image
frequency: 9
level: strong
coverage: 0.784778
common_nodes: [ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/kontext_室内家具产品融图打光_1957494164843851777.json, 平台全量/kontextz最强溶图打光_1950070206964129793.json, 平台全量/kontext去水印_2004032774371721217.json, 平台全量/kontext完美去水印_1991470595630120962.json, 平台全量/kontext换装工作流_1941780121483374593.json, 平台全量/kontext深度图提取_1950934454166552577.json, 平台全量/产品精修 重新打光 极速版 电商产品 拍摄产品一键精修 清除产品表面的灰尘、划痕和微小瑕疵。优化照明_2034854170599104514.json, 平台全量/产品精修_1966408833457401857.json, 平台全量/摄影丨波光粼粼效果_1963218450141384705.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_30

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/kontext_室内家具产品融图打光_1957494164843851777.json、平台全量/kontextz最强溶图打光_1950070206964129793.json、平台全量/kontext去水印_2004032774371721217.json、平台全量/kontext完美去水印_1991470595630120962.json、平台全量/kontext换装工作流_1941780121483374593.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 9 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 8/9 个有
- `PreviewImage` —— 8/9 个有
- `CLIPTextEncode` —— 7/9 个有
- `FluxKontextImageScale` —— 7/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `ResizeLongestToNode` —— 3/9 个有
- `LayerMask: BiRefNetUltraV2` —— 2/9 个有
- `LayerMask: LoadBiRefNetModel` —— 2/9 个有
- `RHHiddenNodes` —— 2/9 个有
- `ImageStitch` —— 1/9 个有
- `easy int` —— 1/9 个有
- `easy seed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 9 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 56% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，9 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
