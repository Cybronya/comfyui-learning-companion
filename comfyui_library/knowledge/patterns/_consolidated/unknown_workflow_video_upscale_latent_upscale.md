---
name: unknown_workflow_video_upscale_latent_upscale
type: Unknown Workflow
frequency: 47
level: strong
coverage: 0.787532
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, VAEDecodeTiled, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/LTX2.3 模型 数字人说话唱歌对口型工作流_2070144070256775169.json, 图片生成/图生图/LTX2.3+Org版++最新数字人说话唱歌对口型++_2072135073440296962.json, 视频生成/图生视频/005.LTX2.3音视融合002.LTX2.3图或文+音生视频_2035354663842746370.json, 视频生成/图生视频/LTX LTX2.3 文生视频 文生MV_2041707361903058945.json, 视频生成/图生视频/LTX2.3 Org版 图片说话唱歌精确对口型 图生视频_2082459555551858689.json, 视频生成/图生视频/LTX2.3 Org版 图片说话唱歌精确对口型_2068287878093955073.json, 视频生成/图生视频/LTX2.3 Org版 图片说话唱歌精确对口型_2069026282452639746.json, 视频生成/图生视频/LTX2.3 Org版 图片说话唱歌精确对口型_2103431205076168706.json, 视频生成/图生视频/LTX2.3 Org版 图片说话唱歌精确对口型_2103455782971990018.json, 视频生成/图生视频/LTX2.3 Org版 图片说话唱歌精确对口型图生视频_2081696395232370690.json, 视频生成/图生视频/LTX2.3 Org版！数字人说话唱歌对口型！B站艾橘溪_2068218768014274561.json, 视频生成/图生视频/LTX2.3 Org版！数字人说话唱歌对口型！_2068294782593626113.json, 视频生成/图生视频/LTX2.3 Org版！数字人说话唱歌对口型！高动态，丝滑运镜！_2068288834533675009.json, 视频生成/图生视频/LTX2.3 图生视频 数字音乐人 图音双驱动_2036255760610496514.json, 视频生成/图生视频/LTX2.3 数字人唱歌 图生视频 智能对口型 极速版  图片音频双驱动_2035160184418471938.json, 视频生成/图生视频/LTX2.3 数字人说话唱歌对口型！_2052644596936650754.json, 视频生成/图生视频/LTX2.3 数字人说话唱歌对口型！_2052992002366689281.json, 视频生成/图生视频/LTX2.3 数字人说话唱歌对口型！_2055189140328722433.json, 视频生成/图生视频/LTX2.3 数字人说话唱歌对口型！_2058724589433352194.json, 视频生成/图生视频/LTX2.3 数字人说话唱歌对口型！_2059186368546430977.json, 视频生成/图生视频/LTX2.3 数字人说话唱歌对口型！_2059884088110174209.json, 视频生成/图生视频/LTX2.3 数字人说话唱歌对口型！_2062789190563225602.json, 视频生成/图生视频/LTX2.3 最强数字人（语音口播）_2080251768956608514.json, 视频生成/图生视频/LTX2.3+Org 加长图生视频High-Quality Image-to-Video_2093890735903956994.json, 视频生成/图生视频/LTX2.3+Org版  最新数字人说话唱歌对口型_2071781935793393665.json, 视频生成/图生视频/LTX2.3单图+音频对口型无字幕_2040333916862685186.json, 视频生成/图生视频/LTX2.3去字幕无字幕版数字人视频说话唱歌对口型ai数字人视频短剧对话数字人视频_2042076729832906754.json, 视频生成/图生视频/LTX2.3对口型 数字人说话唱歌 去字幕+无字幕版_2040953875372445698.json, 视频生成/图生视频/LTX2.3数字人说话唱歌对口型 去字幕+无字幕版_2039930544166805506.json, 视频生成/图生视频/LTX2.3文生MV工作流_2030898825140899842.json, 视频生成/图生视频/LTX2.3文生视频长视频制作文本生成视频mv制作口播视频生成_2037756141316345857.json, 视频生成/图生视频/图生视频-LTX2.3 数字人说话唱歌对口型_2065027141875621889.json, 视频生成/图生视频/数字人_人物唱歌_脱口秀等-LTX2.3图生视频 自适应提示词_2073004728237256705.json, 视频生成/图生视频/数字人_人物唱歌_脱口秀等-LTX2.3图生视频_2071813613165309953.json, 视频生成/图生视频/数字人话 LTX2.3唱歌对口型_2042466020870332417.json, 视频生成/图生视频/最新数字人说话唱歌对口型  LTX2.3+Org版_2071796898314407937.json, 视频生成/图生视频/最新数字人说话唱歌对口型 LTX2.3+Org版_2076471205808394241.json, 视频生成/文生视频/LTX LTX2.3 文生视频 文生MV_2041828761359880193.json, 视频生成/文生视频/LTX2.3 数字人唱歌说话 对口型 图生视频 智能极速版  图片音频双驱动_2035153850771968001.json, 视频生成/文生视频/LTX2.3 文生视频 文生MV_2037069470136541186.json, 视频生成/文生视频/LTX2.3文生MV工作流_2030727534442188801.json, 视频生成/文生视频/LTX2.3文生MV工作流_2032463287467642882.json, 视频生成/文生视频/LTX2.3文生MV工作流_2034249600609034241.json, 视频生成/文生视频/LTX2.3文生MV工作流_2035257169087569922.json, 视频生成/文生视频/【最新加速版】数字人话 LTX2.3唱歌对口型_2043952711799934977.json, 视频生成/文生视频/数字人话 LTX2.3唱歌对口型【最新加速版】_2042470118726311937.json, 音频生成/音频生成/LTX2.3 数字人说话唱歌对口型_2043490102965440514.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale

> 由 `engine/knowledge_consolidation` 从 47 个 workflow 归纳得出（图片生成/图生图/LTX2.3 模型 数字人说话唱歌对口型工作流_2070144070256775169.json、图片生成/图生图/LTX2.3+Org版++最新数字人说话唱歌对口型++_2072135073440296962.json、视频生成/图生视频/005.LTX2.3音视融合002.LTX2.3图或文+音生视频_2035354663842746370.json、视频生成/图生视频/LTX LTX2.3 文生视频 文生MV_2041707361903058945.json、视频生成/图生视频/LTX2.3 Org版 图片说话唱歌精确对口型 图生视频_2082459555551858689.json…）

- **类型**：Unknown Workflow
- **样本数**：47
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 47 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleMath+`
- `SolidMask`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 44/47 个有
- `Int` —— 44/47 个有
- `KSampler` —— 44/47 个有
- `LTX2SamplingPreviewOverride` —— 44/47 个有
- `LTXVPreprocess` —— 44/47 个有
- `MelBandRoFormerModelLoader` —— 44/47 个有
- `MelBandRoFormerSampler` —— 44/47 个有
- `LoadImage` —— 38/47 个有
- `PrimitiveBoolean` —— 36/47 个有
- `DF_Int_to_Float` —— 34/47 个有
- `ImageResizeKJv2` —— 34/47 个有
- `LTX2_NAG` —— 34/47 个有
- `PrimitiveInt` —— 34/47 个有
- `PrimitiveStringMultiline` —— 34/47 个有
- `CM_FloatToInt` —— 32/47 个有
- `JoinStrings` —— 31/47 个有
- `SoundFlow_GetLength` —— 30/47 个有
- `TrimAudioDuration` —— 30/47 个有
- `PreviewAudio` —— 27/47 个有
- `ResizeImagesByLongerEdge` —— 27/47 个有
- `ComfyMathExpression` —— 20/47 个有
- `LTXVAudioVAEDecode` —— 19/47 个有
- `ManualSigmas` —— 19/47 个有
- `ImageAndMaskResizeNode` —— 17/47 个有
- `PrimitiveFloat` —— 15/47 个有
- `LayerUtility: PurgeVRAM` —— 14/47 个有
- `NormalizeAudioLoudness` —— 14/47 个有
- `INTConstant` —— 13/47 个有
- `PathchSageAttentionKJ` —— 13/47 个有
- `easy cleanGpuUsed` —— 13/47 个有
- `easy showAnything` —— 13/47 个有
- `ImageSharpen` —— 10/47 个有
- `Compare` —— 6/47 个有
- `InversionDemoLazySwitch` —— 6/47 个有
- `ResizeImageMaskNode` —— 6/47 个有
- `RH_GetAudioDuration` —— 3/47 个有
- `RTXVideoSuperResolution` —— 3/47 个有
- `PreviewAny` —— 2/47 个有
- `RHLLMChatNode` —— 2/47 个有
- `Textbox` —— 2/47 个有
- `CR Text` —— 1/47 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 44 | 93% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 44 | 100% |
| 采样算法 | euler | - | 44 | 61% |
| 调度器 | simple | - | 44 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.4 | 44 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 44/47 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 44/47 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，44 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，44 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，44 个样本，一致性 61%
- 调度器 最常用 simple，44 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.4，44 个样本，取值集中（一致性 100%）
- 高发问题（44/47 个样本）：Steps较低可能导致细节不足
- 高发问题（44/47 个样本）：发现KSampler但没有VAEDecode
