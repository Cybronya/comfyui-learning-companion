---
name: image_to_image_sampler_clip_unet_23
type: Image To Image
frequency: 11
level: strong
coverage: 0.916727
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext 产品专业打光｜电商_1947606970641670145.json, 图片生成/图生图/Kontext 十大优质lora模型使用_1941855678447382529.json, 图片生成/图生图/Kontext&Lora_1940383341097152513.json, 图片生成/图生图/Kontext+lora角度编辑器_1942022786829467649.json, 图片生成/图生图/Kontext-Lora&ACE++_1940386151624765441.json, 图片生成/图生图/Kontext三视图（三张大图呈现）_1953727580824326145.json, 图片生成/图生图/Kontext闪光灯效果_1953817584930050049.json, 图片生成/图生图/kontext改字-溶图_1953717017230626817.json, 图片生成/图生图/最强真实老照片修复_1947226707453497346.json, 图片生成/图生图/老照片修复2.0版本，一键修复，可搭配去除AI感工作流使用_2027976944700104706.json, 图片生成/图生图/老照片修复，一键修复_2029503656806064129.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_23

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Kontext 产品专业打光｜电商_1947606970641670145.json、图片生成/图生图/Kontext 十大优质lora模型使用_1941855678447382529.json、图片生成/图生图/Kontext&Lora_1940383341097152513.json、图片生成/图生图/Kontext+lora角度编辑器_1942022786829467649.json、图片生成/图生图/Kontext-Lora&ACE++_1940386151624765441.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
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
- `FluxGuidance` —— 10/11 个有
- `LoraLoaderModelOnly` —— 10/11 个有
- `PreviewImage` —— 10/11 个有
- `CR Text` —— 7/11 个有
- `RH_Translator` —— 7/11 个有
- `easy cleanGpuUsed` —— 6/11 个有
- `CR Text Concatenate` —— 5/11 个有
- `FilmGrain` —— 3/11 个有
- `LayerColor: Brightness & Contrast` —— 3/11 个有
- `KepStringLiteral` —— 2/11 个有
- `SDXLEmptyLatentSizePicker+` —— 2/11 个有
- `CR Prompt List` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `LayerUtility: ImageScaleRestore` —— 1/11 个有
- `PIP_图像联结` —— 1/11 个有
- `ShowText|pysssss` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 0.8 - 1 | 11 | 91% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 91% |
| 重绘幅度 | 1 | 0.95 - 1 | 11 | 98% |
| 宽度 | 768x1280 (0.6) | - | 2 | 100% |
| 高度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.8 - 1，11 个样本，取值集中（一致性 91%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 0.95 - 1，11 个样本，取值集中（一致性 98%）
- 宽度 最常用 768x1280 (0.6)，2 个样本，一致性 100%
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.8，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
