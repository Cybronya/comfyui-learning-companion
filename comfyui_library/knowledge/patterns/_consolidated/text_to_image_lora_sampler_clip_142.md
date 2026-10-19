---
name: text_to_image_lora_sampler_clip_142
type: Text To Image
frequency: 7
level: strong
coverage: 0.900429
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/SBAPI MinimaxH3三分镜参考生成视频工作流 多模态输入_2109723354918907905.json, 视频生成/图生视频/SBAPI_MinimaxH3三分镜参考，文生视频图生视频联动_2111195384482721793.json, 视频生成/图生视频/SBAPI_MinimaxH3三连分镜参考出片｜文生视频图生视频一条龙_2111053464666206209.json, 视频生成/图生视频/h3 r2v runninghub tts v2｜图生视频音频驱动生成_2091306513502654466.json, 视频生成/文生视频/H3参考生视频量化加速版文本图像音频视频多模态_2100678580580732929.json, 视频生成/文生视频/多素材联合参考video_minimax_h3_r2v_2085451709555499009.json, 视频生成/文生视频/量化加速参考生视频｜MiniMaxH3 文本图像音视频全参考_2089345982659121153.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_142

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/SBAPI MinimaxH3三分镜参考生成视频工作流 多模态输入_2109723354918907905.json、视频生成/图生视频/SBAPI_MinimaxH3三分镜参考，文生视频图生视频联动_2111195384482721793.json、视频生成/图生视频/SBAPI_MinimaxH3三连分镜参考出片｜文生视频图生视频一条龙_2111053464666206209.json、视频生成/图生视频/h3 r2v runninghub tts v2｜图生视频音频驱动生成_2091306513502654466.json、视频生成/文生视频/H3参考生视频量化加速版文本图像音频视频多模态_2100678580580732929.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 4/7 个有
- `DF_String_Concatenate` —— 3/7 个有
- `DF_Text_Box` —— 3/7 个有
- `JWStringGetLine` —— 3/7 个有
- `JjkConcat` —— 3/7 个有
- `JjkShowText` —— 3/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/7 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 3/7 个有
- `ReplaceString` —— 3/7 个有
- `SaveImage` —— 3/7 个有
- `StringConstant` —— 3/7 个有
- `VHS_LoadVideo` —— 3/7 个有
- `MiniMaxH3AudioLatentControlT8` —— 1/7 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/7 个有
- `easy indexTTSAudioMerge` —— 1/7 个有
- `easy indexTTSGenerate` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
