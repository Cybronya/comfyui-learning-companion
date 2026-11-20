---
name: image_to_image_lora_sampler_clip_32
type: Image To Image
frequency: 10
level: moderate
coverage: 0.9418
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Kontext 二次元-吉卜力-写实风格转换_1938490800030285826.json, 平台全量/Kontext 修改文字_1938542591627714561.json, 平台全量/Kontext 全部_局部擦除物体_1938501426664660993.json, 平台全量/Kontext 古风修图_1952274429877366786.json, 平台全量/Kontext 图片去水印_1938618346013446146.json, 平台全量/Kontext 扩图_图像边界外扩_1945392873346932738.json, 平台全量/Kontext 改变发色_1938534277556404226.json, 平台全量/Kontext 改变图像光线_1938552886198784001.json, 平台全量/Kontext 老照片修复_1938607359499362306.json, 平台全量/kontext扩图简化版_1946211160620457986.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_32

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/Kontext 二次元-吉卜力-写实风格转换_1938490800030285826.json、平台全量/Kontext 修改文字_1938542591627714561.json、平台全量/Kontext 全部_局部擦除物体_1938501426664660993.json、平台全量/Kontext 古风修图_1952274429877366786.json、平台全量/Kontext 图片去水印_1938618346013446146.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
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
- `easy positive` —— 7/10 个有
- `FluxKontextImageScale` —— 3/10 个有
- `DF_Integer` —— 1/10 个有
- `ImagePadForOutpaint` —— 1/10 个有
- `ImagePadKJ` —— 1/10 个有
- `ImpactSwitch` —— 1/10 个有
- `JjkText` —— 1/10 个有
- `easy promptConcat` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 27 | 10 | 40% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 27，10 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（8/10 个样本）：Steps较低可能导致细节不足
