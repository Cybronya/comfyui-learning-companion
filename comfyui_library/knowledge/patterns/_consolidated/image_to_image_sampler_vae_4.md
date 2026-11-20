---
name: image_to_image_sampler_vae_4
type: Image To Image
frequency: 20
level: strong
coverage: 0.9499
common_nodes: [ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, NunchakuFluxDiTLoader, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux1-Kontext-去除图片中的文字_1949048598852972545.json, 图片生成/图生图/Flux1-Kontext人物换背景+背景参考_1948389692900290561.json, 图片生成/图生图/Flux1-Kontext人物换背景_1948386312018636802.json, 图片生成/图生图/Flux1-Kontext单图编辑+Nunchaku+Turbo8步加速-10秒出图_1948149696696070146.json, 图片生成/图生图/Flux1-Kontext单图编辑+Nunchaku加速_1948149597574168578.json, 图片生成/图生图/Flux1-Kontext去人物_1948413311414075394.json, 图片生成/图生图/Flux1-Kontext去人物留背景+人物换背景_1948420688827822082.json, 图片生成/图生图/Flux1-Kontext去除图片中的文字-Nunchaku加速_1948884685205188609.json, 图片生成/图生图/Flux1-Kontext双图编辑+Nunchaku+Turbo8步加速+10秒出图_1948150218222108674.json, 图片生成/图生图/Flux1-Kontext双图编辑+Nunchaku加速_1948148937090838529.json, 图片生成/图生图/Flux1-Kontext移除物品+修复-Nun加速_1949274803111436290.json, 图片生成/图生图/Kontext-极速图像去水印擦除_1982499686877675521.json, 图片生成/图生图/KontextNunchakuDev转绘Abbott Fuller Graves风格_1940994557704355841.json, 图片生成/图生图/KontextNunchakuDev转绘墨绘长笔画_1940998785357213697.json, 图片生成/图生图/KontextNunchakuDev转绘英雄幻想风格_1941004455217414145.json, 图片生成/图生图/ani①-Kontext转真人_1945084253686386689.json, 图片生成/图生图/一键调整人物方向Flux+Kontext_2044605376926064641.json, 图片生成/文生图/Flux Kontext  人物模特镜头方向调整_1944642913160843265.json, 图片生成/文生图/Flux Kontext 人物方向调整_1942757866497617921.json, 数字人/数字人/01.Flux Kontext 人物方向调整_许老师专用_1976297487822622721.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_4

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/Flux1-Kontext-去除图片中的文字_1949048598852972545.json、图片生成/图生图/Flux1-Kontext人物换背景+背景参考_1948389692900290561.json、图片生成/图生图/Flux1-Kontext人物换背景_1948386312018636802.json、图片生成/图生图/Flux1-Kontext单图编辑+Nunchaku+Turbo8步加速-10秒出图_1948149696696070146.json、图片生成/图生图/Flux1-Kontext单图编辑+Nunchaku加速_1948149597574168578.json…）

- **类型**：Image To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 20 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageStitch` —— 17/20 个有
- `CLIPTextEncode` —— 16/20 个有
- `NunchakuFluxLoraLoader` —— 16/20 个有
- `ImageConcanate` —— 11/20 个有
- `RH_Translator` —— 8/20 个有
- `ShowText|pysssss` —— 8/20 个有
- `LoadImageOutput` —— 6/20 个有
- `RHHiddenNodes` —— 6/20 个有
- `Text Multiline` —— 6/20 个有
- `CR Prompt Text` —— 5/20 个有
- `GoogleTranslateTextNode` —— 5/20 个有
- `PreviewImage` —— 4/20 个有
- `ModelSamplingFlux` —— 3/20 个有
- `EmptySD3LatentImage` —— 1/20 个有
- `ttN concat` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 20 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 20 | 100% |
| 采样算法 | euler | - | 20 | 100% |
| 调度器 | simple | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，20 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，20 个样本，一致性 100%
- 调度器 最常用 simple，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
