---
name: unknown_workflow_video_lora_sampler_152
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.806167
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, JWInteger, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/图生视频V1_2047405386377990145.json, 视频生成/图生视频/大明动画风格 长时间讲话 带音频_1970454235139743746.json, 视频生成/图生视频/对口型数字人Infinite+Talk 音色克隆带语气情感_2039589897626984450.json, 视频生成/图生视频/对口型数字人Infinite+Talk_2052766629263618049.json, 视频生成/图生视频/数字人_音画同步_对口型 Infinite Talk_2004160279342686209.json, 视频生成/图生视频/百组动态！Infinite Talk极速高质量提示词调度动作控制图生视频KTV数字人V2_1960048260402589698.json, 视频生成/图生视频/稳定的唱歌对口型_2029971317079937026.json, 视频生成/图生视频/视频-图生视频+数字人对口型_1960792886629601281.json, 视频生成/图生视频/音色克隆 对口型数字人Infinite+Talk 带语气情感_2041353094105141250.json, 视频生成/图生视频/（再说一遍）Infinite Talk极速高质量提示词调度动作控制图生视频KTV数字人V1_1971615313714475009.json, 视频生成/图生视频/（别读博版）Infinite Talk极速高质量提示词调度动作控制图生视频KTV数字人V1_1961304716842045442.json, 音频生成/音频生成/对口型数字人Infinite+Talk_1977882176555470849.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_152

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/图生视频V1_2047405386377990145.json、视频生成/图生视频/大明动画风格 长时间讲话 带音频_1970454235139743746.json、视频生成/图生视频/对口型数字人Infinite+Talk 音色克隆带语气情感_2039589897626984450.json、视频生成/图生视频/对口型数字人Infinite+Talk_2052766629263618049.json、视频生成/图生视频/数字人_音画同步_对口型 Infinite Talk_2004160279342686209.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 12 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `JWInteger`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/12 个有
- `PreviewAny` —— 11/12 个有
- `CLIPTextEncode` —— 1/12 个有
- `ConcatTextOfUtils` —— 1/12 个有
- `GetNode` —— 1/12 个有
- `ImageBatch` —— 1/12 个有
- `ImageFromBatch` —— 1/12 个有
- `KSampler` —— 1/12 个有
- `VAEDecode` —— 1/12 个有
- `VRGDG_AudioCropTime` —— 1/12 个有
- `WanInfiniteTalkToVideo` —— 1/12 个有
- `easy indexAnything` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | normal | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
