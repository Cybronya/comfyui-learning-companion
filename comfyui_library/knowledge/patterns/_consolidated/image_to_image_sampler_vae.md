---
name: image_to_image_sampler_vae
type: Image To Image
frequency: 43
level: strong
coverage: 0.913628
common_nodes: [ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, NunchakuFluxDiTLoader, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux1-Kontext-去除图片中的文字_1949048598852972545.json, 图片生成/图生图/Flux1-Kontext人物换背景+背景参考_1948389692900290561.json, 图片生成/图生图/Flux1-Kontext人物换背景_1948386312018636802.json, 图片生成/图生图/Flux1-Kontext单图编辑+Nunchaku+Turbo8步加速-10秒出图_1948149696696070146.json, 图片生成/图生图/Flux1-Kontext单图编辑+Nunchaku加速_1948149597574168578.json, 图片生成/图生图/Flux1-Kontext去人物_1948413311414075394.json, 图片生成/图生图/Flux1-Kontext去人物留背景+人物换背景_1948420688827822082.json, 图片生成/图生图/Flux1-Kontext去除图片中的文字-Nunchaku加速_1948884685205188609.json, 图片生成/图生图/Flux1-Kontext双图编辑+Nunchaku+Turbo8步加速+10秒出图_1948150218222108674.json, 图片生成/图生图/Flux1-Kontext双图编辑+Nunchaku加速_1948148937090838529.json, 图片生成/图生图/Flux1-Kontext移除物品+修复-Nun加速_1949274803111436290.json, 图片生成/图生图/Kontext-极速图像去水印擦除_1982499686877675521.json, 图片生成/图生图/KontextNunchakuDev转绘Abbott Fuller Graves风格_1940994557704355841.json, 图片生成/图生图/KontextNunchakuDev转绘墨绘长笔画_1940998785357213697.json, 图片生成/图生图/KontextNunchakuDev转绘英雄幻想风格_1941004455217414145.json, 图片生成/图生图/ani①-Kontext转真人_1945084253686386689.json, 图片生成/图生图/一键调整人物方向Flux+Kontext_2044605376926064641.json, 图片生成/文生图/Flux Kontext  人物模特镜头方向调整_1944642913160843265.json, 图片生成/文生图/Flux Kontext 人物方向调整_1942757866497617921.json, 平台全量/Flux Kontext Dev  JOJO风格转绘_1941893274871480322.json, 平台全量/Flux Kontext Dev  乐高风格转绘_1941895184881971201.json, 平台全量/Flux Kontext Dev  吉卜力风格转绘_1941889356175196161.json, 平台全量/Flux Kontext Dev  日本剪贴画风格转绘_1941891060668985345.json, 平台全量/Flux Kontext Dev  油画风格转绘_1941899918275670018.json, 平台全量/Flux Kontext Dev  粘土玩具风格转绘_1941865826519773186.json, 平台全量/Flux Kontext Dev  线条风格转绘_1941896517370408962.json, 平台全量/Flux Kontext Dev  面料风格转绘_1941886497606025218.json, 平台全量/Flux Kontext Dev  马卡龙风格转绘_1941898209977593857.json, 平台全量/Flux Kontext Dev 3D风格转绘_1942455350408974338.json, 平台全量/Flux Kontext Dev 中国水墨风格转绘_1942418534527873026.json, 平台全量/Flux Kontext Dev 像素风格转绘_1942244860311310337.json, 平台全量/Flux Kontext Dev 像素风格转绘_1942250141862539266.json, 平台全量/Flux Kontext Dev 剪纸风格转绘_1942236128088895490.json, 平台全量/Flux Kontext Dev 史努比风格转绘_1942406204217831425.json, 平台全量/Flux Kontext Dev 多边形风格转绘_1942247975227953153.json, 平台全量/Flux Kontext Dev 折纸风格转绘_1942416587788062721.json, 平台全量/Flux Kontext Dev 梵高风格转绘_1942415451768958978.json, 平台全量/Flux Kontext Dev 毕加索风格转绘_1942241240966696961.json, 平台全量/Flux Kontext Dev 毕加索风格转绘_1942251559910838274.json, 平台全量/Flux Kontext Dev 波普艺术风格转绘_1942376304949800962.json, 平台全量/Flux Kontext Dev 瑞克和莫蒂风格转绘_1942381253951696897.json, 平台全量/Flux Kontext Dev 矢量风格转绘_1942410494026133505.json, 平台全量/Flux Kontext Dev 美国卡通风格转绘_1941873754752630785.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae

> 由 `engine/knowledge_consolidation` 从 43 个 workflow 归纳得出（图片生成/图生图/Flux1-Kontext-去除图片中的文字_1949048598852972545.json、图片生成/图生图/Flux1-Kontext人物换背景+背景参考_1948389692900290561.json、图片生成/图生图/Flux1-Kontext人物换背景_1948386312018636802.json、图片生成/图生图/Flux1-Kontext单图编辑+Nunchaku+Turbo8步加速-10秒出图_1948149696696070146.json、图片生成/图生图/Flux1-Kontext单图编辑+Nunchaku加速_1948149597574168578.json…）

- **类型**：Image To Image
- **样本数**：43
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 43 个 workflow 都包含：
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
- `ImageStitch` —— 40/43 个有
- `CLIPTextEncode` —— 39/43 个有
- `ImageConcanate` —— 34/43 个有
- `RHHiddenNodes` —— 30/43 个有
- `LoadImageOutput` —— 29/43 个有
- `CR Prompt Text` —— 28/43 个有
- `GoogleTranslateTextNode` —— 28/43 个有
- `PreviewImage` —— 27/43 个有
- `ShowText` —— 24/43 个有
- `easy promptConcat` —— 24/43 个有
- `NunchakuFluxLoraLoader` —— 15/43 个有
- `RH_Translator` —— 8/43 个有
- `ShowText|pysssss` —— 8/43 个有
- `Text Multiline` —— 6/43 个有
- `ModelSamplingFlux` —— 3/43 个有
- `EmptySD3LatentImage` —— 1/43 个有
- `ttN concat` —— 1/43 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 43 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 43 | 100% |
| 采样算法 | euler | - | 43 | 100% |
| 调度器 | simple | - | 43 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 43 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/43 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，43 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，43 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，43 个样本，一致性 100%
- 调度器 最常用 simple，43 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，43 个样本，取值集中（一致性 100%）
