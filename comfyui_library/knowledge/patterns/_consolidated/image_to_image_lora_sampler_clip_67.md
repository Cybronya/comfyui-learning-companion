---
name: image_to_image_lora_sampler_clip_67
type: Image To Image
frequency: 6
level: strong
coverage: 0.941333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/服装衣物生成3D镂空图_1980917939945783297.json, 图片生成/图生图/版画艺术生成器_1996222237315309569.json, 图片生成/文生图/真人变假模_1980925614649724929.json, 平台全量/Kontext-老照片修复_1946963516941328385.json, 平台全量/Kontext老照片修复_V1.0版本_1950795927500038145.json, 平台全量/kontext一键取衣去人（去掉人物只留衣服）_1941038033233985537.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_67

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/服装衣物生成3D镂空图_1980917939945783297.json、图片生成/图生图/版画艺术生成器_1996222237315309569.json、图片生成/文生图/真人变假模_1980925614649724929.json、平台全量/Kontext-老照片修复_1946963516941328385.json、平台全量/Kontext老照片修复_V1.0版本_1950795927500038145.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ShowText|pysssss` —— 5/6 个有
- `Text Multiline` —— 5/6 个有
- `ImageConcatMulti` —— 4/6 个有
- `ImageStitch` —— 2/6 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/6 个有
- `LayerUtility: ImageAutoCrop V2` —— 2/6 个有
- `ConstrainImage|pysssss` —— 1/6 个有
- `ImageResize+` —— 1/6 个有
- `LayerUtility: CropByMask` —— 1/6 个有
- `PrimitiveFloat` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `ttN concat` —— 1/6 个有
- `ttN text` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
