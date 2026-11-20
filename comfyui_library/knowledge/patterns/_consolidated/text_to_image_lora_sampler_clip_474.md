---
name: text_to_image_lora_sampler_clip_474
type: Text To Image
frequency: 4
level: moderate
coverage: 0.91475
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Nunchaku_苗族服装生成_1935576346364149761.json, 图片生成/文生图/nunchaku加速文生图节省RH币_1933900850979102721.json, 图片生成/文生图/文生图nunchaku Krea_1951256714563760129.json, 图片生成/文生图/沙雕动画角色抽卡器 双节棍_1956292377864491009.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_474

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Nunchaku_苗族服装生成_1935576346364149761.json、图片生成/文生图/nunchaku加速文生图节省RH币_1933900850979102721.json、图片生成/文生图/文生图nunchaku Krea_1951256714563760129.json、图片生成/文生图/沙雕动画角色抽卡器 双节棍_1956292377864491009.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `FluxGuidance` —— 3/4 个有
- `NunchakuTextEncoderLoader` —— 3/4 个有
- `RH_Translator` —— 3/4 个有
- `ModelSamplingFlux` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `JjkText` —— 1/4 个有
- `LatentUpscaleBy` —— 1/4 个有
- `NunchakuTextEncoderLoaderV2` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `Text Concatenate` —— 1/4 个有
- `Text Random Line` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 744 | 576 - 1080 | 4 | 77% |
| 高度 | 1152 | 1024 - 1920 | 4 | 72% |
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 0.5 - 1 | 4 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 744，观测区间 576 - 1080，4 个样本
- 高度 中位数 1152，观测区间 1024 - 1920，4 个样本
- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，4 个样本
