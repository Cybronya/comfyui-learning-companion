---
name: image_to_image_lora_sampler_vae_5
type: Image To Image
frequency: 13
level: strong
coverage: 0.959154
common_nodes: [ConditioningZeroOut, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux Kontext-真人转动漫 Nunchaku加速版_1964121930297167874.json, 图片生成/图生图/Flux+Kontext-高清还原（Nunchaku）_1968246375500664834.json, 图片生成/图生图/Flux1-Kontext-去除图片中的文字_1949048598852972545.json, 图片生成/图生图/Flux1-Kontext人物换背景+背景参考_1948389692900290561.json, 图片生成/图生图/Flux1-Kontext人物换背景_1948386312018636802.json, 图片生成/图生图/Flux1-Kontext去人物_1948413311414075394.json, 图片生成/图生图/Flux1-Kontext去人物留背景+人物换背景_1948420688827822082.json, 图片生成/图生图/Flux1-Kontext去除图片中的文字-Nunchaku加速_1948884685205188609.json, 图片生成/图生图/Kontext扩图（扩下半身）_1968240084396978177.json, 图片生成/图生图/ani①-Kontext转真人_1945084253686386689.json, 图片生成/图生图/一键调整人物方向Flux+Kontext_2044605376926064641.json, 图片生成/文生图/Flux Kontext  人物模特镜头方向调整_1944642913160843265.json, 图片生成/文生图/Flux Kontext 人物方向调整_1942757866497617921.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_5

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Flux Kontext-真人转动漫 Nunchaku加速版_1964121930297167874.json、图片生成/图生图/Flux+Kontext-高清还原（Nunchaku）_1968246375500664834.json、图片生成/图生图/Flux1-Kontext-去除图片中的文字_1949048598852972545.json、图片生成/图生图/Flux1-Kontext人物换背景+背景参考_1948389692900290561.json、图片生成/图生图/Flux1-Kontext人物换背景_1948386312018636802.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 13 个 workflow 都包含：
- `ConditioningZeroOut`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 12/13 个有
- `ImageStitch` —— 11/13 个有
- `ImageConcanate` —— 10/13 个有
- `CLIPTextEncode` —— 9/13 个有
- `CR Prompt Text` —— 6/13 个有
- `RHHiddenNodes` —— 6/13 个有
- `GoogleTranslateTextNode` —— 5/13 个有
- `PreviewImage` —— 5/13 个有
- `LoadImageOutput` —— 4/13 个有
- `EmptySD3LatentImage` —— 1/13 个有
- `ImagePadForOutpaint` —— 1/13 个有
- `LayerUtility: PurgeVRAM` —— 1/13 个有
- `NunchakuTextEncoderLoaderV2` —— 1/13 个有
- `SUPIR_Upscale` —— 1/13 个有
- `Text Multiline` —— 1/13 个有
- `workflow>MaskColor` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 13 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，13 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
