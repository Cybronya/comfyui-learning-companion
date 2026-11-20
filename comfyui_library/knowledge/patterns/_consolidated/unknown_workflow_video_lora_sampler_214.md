---
name: unknown_workflow_video_lora_sampler_214
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8304
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/数字人说话 图生视频_2017055239785947137.json, 数字人/数字人/文本+语音生成高动态视频Lightx2v+Rcm+FlashVSR(加速版)_2002711904197984257.json, 视频生成/图生视频/(JK装版)Infinite Talk极速高质量提示词调度动作控制图生视频数字人V1_1978860763139969026.json, 视频生成/图生视频/(KJ版-分组动作)Infinite Talk无限时长动态加强版V1_2018971911878873089.json, 视频生成/图生视频/(LTX训练专用版FPS24）Infinite talk数字人素材（5秒121帧）_2035984578132840449.json, 视频生成/图生视频/(Supermate优化）index tts Infinite talk数字人动态加强高版V1_2017601660696137730.json, 视频生成/图生视频/InfiniteTalk（Lightx2v+Rcm） -数字人唱歌-长时稳定不变色_2014949900475174914.json, 视频生成/图生视频/【阿良绘】数字人讲话（图生视频）_高动态Infinite talk（Lightx2v+Rcm）_1960200175715299330.json, 视频生成/图生视频/跨模态仿OVI无限时长图生视频含配音数字人工作流V1（支持中文）_1974878137764982786.json, 视频生成/文生视频/(Supermate）Index tts Infinite talk数字人动态加强高版V2（文生视频加音画同步）_2020157316225572866.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_214

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（数字人/数字人/数字人说话 图生视频_2017055239785947137.json、数字人/数字人/文本+语音生成高动态视频Lightx2v+Rcm+FlashVSR(加速版)_2002711904197984257.json、视频生成/图生视频/(JK装版)Infinite Talk极速高质量提示词调度动作控制图生视频数字人V1_1978860763139969026.json、视频生成/图生视频/(KJ版-分组动作)Infinite Talk无限时长动态加强版V1_2018971911878873089.json、视频生成/图生视频/(LTX训练专用版FPS24）Infinite talk数字人素材（5秒121帧）_2035984578132840449.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 10 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 8/10 个有
- `CR Prompt Text` —— 7/10 个有
- `JWInteger` —— 7/10 个有
- `JWFloat` —— 5/10 个有
- `Audio Duration (mtb)` —— 3/10 个有
- `CR Text` —— 3/10 个有
- `INTConstant` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `SaveAudio` —— 3/10 个有
- `easy downloadIndexTTSAndLoadModel` —— 3/10 个有
- `easy indexTTSGenerateSimple` —— 3/10 个有
- `DF_Float` —— 2/10 个有
- `GetImageSize` —— 2/10 个有
- `Label (rgthree)` —— 2/10 个有
- `SimpleMath+` —— 2/10 个有
- `CLIPLoader` —— 1/10 个有
- `CLIPTextEncode` —— 1/10 个有
- `ConditioningZeroOut` —— 1/10 个有
- `EmptyLatentImage` —— 1/10 个有
- `FlashVSRNode` —— 1/10 个有
- `Float` —— 1/10 个有
- `FloatConstant` —— 1/10 个有
- `KSamplerAdvanced` —— 1/10 个有
- `LayerUtility: PurgeVRAM` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `MemoryCleaner` —— 1/10 个有
- `UNETLoader` —— 1/10 个有
- `VAEDecode` —— 1/10 个有
- `VAELoader` —— 1/10 个有
- `easy clearCacheAll` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 1 | 100% |
| Prompt 约束强度(CFG) | 10 | - | 1 | 100% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | euler | - | 1 | 100% |
| 重绘幅度 | simple | - | 1 | 100% |
| 宽度 | 1280 | - | 1 | 100% |
| 高度 | 720 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
