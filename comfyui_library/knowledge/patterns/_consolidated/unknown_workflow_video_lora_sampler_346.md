---
name: unknown_workflow_video_lora_sampler_346
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.735
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, GetNode, ImageResizeKJv2, Int, LayerUtility: PurgeVRAM, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SaveAudio, SetNode, SparkTTSClone, Text Multiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [数字人/数字人/数字人-音频_文本驱动（带音色模拟功能）支持动物_2004212445377953794.json, 视频生成/图生视频/AI动物说_2043873863750127617.json, 视频生成/图生视频/AI动物说话=B站艾橘溪_1963961319592480770.json, 视频生成/图生视频/最新3.0AI动物说话（懒人版）_2065443186113339394.json, 视频生成/图生视频/音频文本驱动生成数字人对口型数字人视频生成支持动物说话视频生成声音克隆视频生成_2011517441985220610.json, 视频生成/文生视频/AI动物说话=B站艾橘溪_1970041990975025153.json, 音频生成/音频生成/数字人音频_文本驱动 带音色模仿 支持动物Q版 卡通角色 InfiniteTalk-Wan2.2_1999708121922760705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_346

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/数字人-音频_文本驱动（带音色模拟功能）支持动物_2004212445377953794.json、视频生成/图生视频/AI动物说_2043873863750127617.json、视频生成/图生视频/AI动物说话=B站艾橘溪_1963961319592480770.json、视频生成/图生视频/最新3.0AI动物说话（懒人版）_2065443186113339394.json、视频生成/图生视频/音频文本驱动生成数字人对口型数字人视频生成支持动物说话视频生成声音克隆视频生成_2011517441985220610.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `Int`
- `LayerUtility: PurgeVRAM`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SaveAudio`
- `SetNode`
- `SparkTTSClone`
- `Text Multiline`
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
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `If ANY execute A else B` —— 4/7 个有
- `Int2Any_AS` —— 4/7 个有
- `PrimitiveInt` —— 4/7 个有
- `Any Switch (rgthree)` —— 3/7 个有
- `CR String To Number` —— 3/7 个有
- `CR Text` —— 3/7 个有
- `Fast Groups Muter (rgthree)` —— 3/7 个有
- `ImageConcatMulti` —— 3/7 个有
- `easy anythingIndexSwitch` —— 3/7 个有
- `CR Integer To String` —— 2/7 个有
- `CR Prompt Text` —— 2/7 个有
- `IndexTTS2Run` —— 2/7 个有
- `JWInteger` —— 2/7 个有
- `MathExpression|pysssss` —— 2/7 个有
- `Random Number` —— 2/7 个有
- `ShowText|pysssss` —— 2/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
