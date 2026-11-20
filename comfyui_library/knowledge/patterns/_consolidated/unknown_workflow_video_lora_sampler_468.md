---
name: unknown_workflow_video_lora_sampler_468
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8808
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LayerUtility: PurgeVRAM V2, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewImage, PrimitiveStringMultiline, RoundNode, SaveAudio, SoundFlow_GetLength, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/口播数字人 InfiniteTalk + IndexTTS2，远程加载版_2030935834236559362.json, 数字人/数字人/最强口播数字人 InfiniteTalk + IndexTTS-2_2074771103767158786.json, 视频生成/图生视频/Alan实测 InfiniteTalk + IndexTTS-2_1984183697027039233.json, 视频生成/图生视频/口播数字人天花板  InfiniteTalk 加IndexTTS2_1968328502552473602.json, 视频生成/图生视频/数字人口播_2057106913065787393.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_468

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/口播数字人 InfiniteTalk + IndexTTS2，远程加载版_2030935834236559362.json、数字人/数字人/最强口播数字人 InfiniteTalk + IndexTTS-2_2074771103767158786.json、视频生成/图生视频/Alan实测 InfiniteTalk + IndexTTS-2_1984183697027039233.json、视频生成/图生视频/口播数字人天花板  InfiniteTalk 加IndexTTS2_1968328502552473602.json、视频生成/图生视频/数字人口播_2057106913065787393.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM V2`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RoundNode`
- `SaveAudio`
- `SoundFlow_GetLength`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `IndexTTS2Run` —— 4/5 个有
- `LoadAudio` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `PrimitiveString` —— 4/5 个有
- `FFmpeg_LoadAudioFromURL_JX` —— 1/5 个有
- `FFmpeg_LoadImageFromURL_JX` —— 1/5 个有
- `IndexTTSNode` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
