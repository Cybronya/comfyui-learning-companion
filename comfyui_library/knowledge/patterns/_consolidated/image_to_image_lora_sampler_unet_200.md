---
name: image_to_image_lora_sampler_unet_200
type: Image To Image
frequency: 4
level: strong
coverage: 0.89475
common_nodes: [CFGNorm, CLIPLoader, CR Text, ConstrainImage|pysssss, DWPreprocessor, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RH_Captioner, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptConcat, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Qwen-Edit 人物姿态迁移 动作一致性_1980543189520175106.json, 平台全量/Qwen-Edit 姿态完美迁移 人物一致性  完美动作姿态控制  qwen edit 千问最强姿势_2008356352795615234.json, 平台全量/人物一致性 姿态完美迁移 _ Qwen-Edit_2509_1890318707854548994.json, 平台全量/人物一致性 姿态迁移 _ Qwen-Edit_2511_1950168498037284865.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_200

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/Qwen-Edit 人物姿态迁移 动作一致性_1980543189520175106.json、平台全量/Qwen-Edit 姿态完美迁移 人物一致性  完美动作姿态控制  qwen edit 千问最强姿势_2008356352795615234.json、平台全量/人物一致性 姿态完美迁移 _ Qwen-Edit_2509_1890318707854548994.json、平台全量/人物一致性 姿态迁移 _ Qwen-Edit_2511_1950168498037284865.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `ConstrainImage|pysssss`
- `DWPreprocessor`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RH_Captioner`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptConcat`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 3/4 个有
- `ImitationHueNode` —— 3/4 个有
- `Label (rgthree)` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
