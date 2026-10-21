---
name: text_to_image_lora_sampler_clip_19
type: Text To Image
frequency: 24
level: strong
coverage: 0.883542
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3_24G_3refs_声音参考｜低显存多参考图生视频_2106984789743063042.json, 视频生成/图生视频/H3参考生视频量化加速版文本图像音频视频多模态_2100640992356556801.json, 视频生成/图生视频/H3图生视频8步工作流 高效视频生成工具_2100275409492467713.json, 视频生成/图生视频/H3图生视频加速版｜快速高质量视频直出生成_2094902804635799554.json, 视频生成/图生视频/H3图生视频首尾帧控制原生音频两张图变一段电影_2100681745967435778.json, 视频生成/图生视频/H3多图参考与声音参考视频工作流24G三图参考结构，图生视频角色短片方案_2107244941524168705.json, 视频生成/图生视频/H3多图参考与声音参考视频工作流24G三图参考结构，图生视频角色短片方案_2107461389559357441.json, 视频生成/图生视频/H3多图参考生视频 视频生视频图生视频创作_2100303663238574081.json, 视频生成/图生视频/H3开源加速版多参文生视频图生视频多宫格稳定出片漫剧制作方案_2106491061026779138.json, 视频生成/图生视频/H3开源加速版多参文生视频图生视频，多宫格稳定出片适用于漫剧 制作_2102835082758279169.json, 视频生成/图生视频/H3开源加速版海螺多参文生视频图生视频漫剧 多宫格稳定出片方案_2106478696466046978.json, 视频生成/图生视频/H3开源加速版海螺多参文生视频图生视频漫剧短剧多宫格稳定出片方案_2106506103612858369.json, 视频生成/图生视频/H3开源加速版海螺多参文生视频图生视频漫剧短剧视频H3多宫格稳定出片加速版MiniMax_2099068104457416705.json, 视频生成/图生视频/H3开源加速版海螺多参文生视频图生视频漫剧短剧视频H3多宫格稳定出片加速版MiniMax_2099074502104805378.json, 视频生成/图生视频/H3开源加速版海螺多参流｜漫剧短剧多宫格稳定出片，MiniMax速度加持_2099533253412745217.json, 视频生成/图生视频/H3文生视频加速版｜快速直出高质量视频生成_2094509372390076418.json, 视频生成/图生视频/H3角色替换图生视频｜视频人物一键换脸替换生成_2088772291898466305.json, 视频生成/图生视频/H3角色替换图生视频｜视频人物一键换脸替换生成_2090466751896178689.json, 视频生成/图生视频/MINIMAX H3多模态生视频 参考图像视频音频全接口 视频生视频强机_2105036316378484738.json, 视频生成/图生视频/MINIMAX-H3多模态生视频｜参考图像视频音频全接口｜视频生视频强机_2104443942606561282.json, 视频生成/图生视频/MiniMax H3参考生视频｜Sage加速高质量生成_2095214729747853313.json, 视频生成/图生视频/MiniMax H3图生视频｜Sage加速高质量直出_2095219197193318401.json, 视频生成/图生视频/Sage加速图生视频｜MiniMax H3数字人处理2608_2095495228194115585.json, 视频生成/图生视频/h3图生视频加速版快速出片高效生成工作流_2088357034935808002.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_19

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（视频生成/图生视频/H3_24G_3refs_声音参考｜低显存多参考图生视频_2106984789743063042.json、视频生成/图生视频/H3参考生视频量化加速版文本图像音频视频多模态_2100640992356556801.json、视频生成/图生视频/H3图生视频8步工作流 高效视频生成工具_2100275409492467713.json、视频生成/图生视频/H3图生视频加速版｜快速高质量视频直出生成_2094902804635799554.json、视频生成/图生视频/H3图生视频首尾帧控制原生音频两张图变一段电影_2100681745967435778.json…）

- **类型**：Text To Image
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 24 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 23/24 个有
- `VAEDecodeAudio` —— 22/24 个有
- `ComfyMathExpression` —— 21/24 个有
- `PrimitiveFloat` —— 21/24 个有
- `ResolutionSelector` —— 21/24 个有
- `PrimitiveStringMultiline` —— 20/24 个有
- `孤海注释` —— 19/24 个有
- `CreateVideo` —— 17/24 个有
- `MiniMaxH3ReferenceToVideo` —— 17/24 个有
- `SaveImage` —— 17/24 个有
- `SaveVideo` —— 17/24 个有
- `VHS_VideoCombine` —— 17/24 个有
- `PathchSageAttentionKJ` —— 13/24 个有
- `EasyCache` —— 11/24 个有
- `LoadAudio` —— 10/24 个有
- `Fast Groups Bypasser (rgthree)` —— 7/24 个有
- `FlashVSRNode` —— 7/24 个有
- `LoraLoaderBypassModelOnly` —— 7/24 个有
- `MiniMaxH3ImageToVideo` —— 7/24 个有
- `ModelPatchTorchSettings` —— 7/24 个有
- `Sleep` —— 7/24 个有
- `VHS_LoadVideo` —— 6/24 个有
- `EmptyImage` —— 5/24 个有
- `PreviewImage` —— 5/24 个有
- `SolAttnPatch` —— 5/24 个有
- `FlashVSRInitPipe` —— 3/24 个有
- `FlashVSRNodeAdv` —— 3/24 个有
- `PrimitiveInt` —— 3/24 个有
- `VAEDecodeTiled` —— 3/24 个有
- `CR Prompt Text` —— 2/24 个有
- `GetImageSize` —— 2/24 个有
- `ImageScaleToTotalPixels` —— 2/24 个有
- `PainterVRAM` —— 2/24 个有
- `easy showAnything` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 24 | 100% |
| 高度 | 80 | 80 - 80 | 24 | 100% |
| 采样步数 | 4 | 4 - 4 | 24 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 24 | 100% |
| 采样算法 | er_sde | - | 24 | 100% |
| 调度器 | beta | - | 24 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 38/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，24 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，24 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，24 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，24 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，24 个样本，一致性 100%
- 调度器 最常用 beta，24 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 高发问题（38/24 个样本）：Steps较低可能导致细节不足
