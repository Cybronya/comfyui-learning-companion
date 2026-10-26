---
name: image_to_image_lora_sampler_clip_77
type: Image To Image
frequency: 4
level: strong
coverage: 0.9715
common_nodes: [CLIPTextEncode, CR Text Concatenate, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/千府AI建筑鸟瞰图一键工作流_1962384837388668930.json, 图片生成/图生图/最强真实老照片修复_1947226707453497346.json, 图片生成/图生图/老照片修复2.0版本，一键修复，可搭配去除AI感工作流使用_2027976944700104706.json, 图片生成/图生图/老照片修复，一键修复_2029503656806064129.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_77

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/千府AI建筑鸟瞰图一键工作流_1962384837388668930.json、图片生成/图生图/最强真实老照片修复_1947226707453497346.json、图片生成/图生图/老照片修复2.0版本，一键修复，可搭配去除AI感工作流使用_2027976944700104706.json、图片生成/图生图/老照片修复，一键修复_2029503656806064129.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text Concatenate`
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
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `FilmGrain` —— 3/4 个有
- `LayerColor: Brightness & Contrast` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `RH_Translator` —— 3/4 个有
- `DF_Image_scale_by_ratio` —— 1/4 个有
- `KontextArchPresetMain` —— 1/4 个有
- `NunchakuFluxDiTLoader` —— 1/4 个有
- `NunchakuTextEncoderLoaderV2` —— 1/4 个有
- `Text` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 0.8 | 0.8 - 1 | 4 | 90% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 0.95 | 0.5 - 0.95 | 4 | 77% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 0.8，观测区间 0.8 - 1，4 个样本，取值集中（一致性 90%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 0.95，观测区间 0.5 - 0.95，4 个样本
- 风险：Prompt 约束强度(CFG) 观测到 0.8，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
