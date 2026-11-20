---
name: image_to_image_sampler_clip_unet_23
type: Image To Image
frequency: 14
level: strong
coverage: 0.895286
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/🧙Kontext完美扩图工作流【扩图LORA】🍧_1945310376504512514.json, 图片生成/文生图/去除水印_2090086272101605377.json, 图片生成/文生图/质感提升kontext工作流万物提升_1985614052636479490.json, 平台全量/Flux.1 Kontext 一键商品生背景 V1.0_1968962581920694274.json, 平台全量/KONTEXT换背景_1967862594251948033.json, 平台全量/Kontext Dev老照片修复（修复划痕破损、照片着色））_1940094882851540993.json, 平台全量/Kontext Dev自动去水印-高效、干净_1940080842180050946.json, 平台全量/Kontext-本地版-中文输入_1938417578668916738.json, 平台全量/【超强实用】kontext 智能一键换背景_1961672060466565122.json, 平台全量/一键转简约风格插画_1955601224260206593.json, 平台全量/扩图工作流_1963803929233674241.json, 平台全量/换背景kontext_1950692741019815937.json, 平台全量/老旧照片修复kontext_1950807278670782466.json, 平台全量/🧙Kontext完美扩图工作流【扩图LORA】🍧_1950010151581474817.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_23

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/🧙Kontext完美扩图工作流【扩图LORA】🍧_1945310376504512514.json、图片生成/文生图/去除水印_2090086272101605377.json、图片生成/文生图/质感提升kontext工作流万物提升_1985614052636479490.json、平台全量/Flux.1 Kontext 一键商品生背景 V1.0_1968962581920694274.json、平台全量/KONTEXT换背景_1967862594251948033.json…）

- **类型**：Image To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 14 个 workflow 都包含：
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
- `FluxKontextImageScale` —— 12/14 个有
- `LoraLoaderModelOnly` —— 10/14 个有
- `PreviewImage` —— 10/14 个有
- `RH_Translator` —— 8/14 个有
- `easy imageConcat` —— 5/14 个有
- `ConstrainImage|pysssss` —— 4/14 个有
- `ImageConcanate` —— 3/14 个有
- `ImagePadKJ` —— 3/14 个有
- `JWImageResizeByLongerSide` —— 2/14 个有
- `JWInteger` —— 2/14 个有
- `Image Compare (mtb)` —— 1/14 个有
- `RepeatLatentBatch` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 14 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 79% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 79%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
