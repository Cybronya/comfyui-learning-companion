---
name: unknown_workflow_video_lora_sampler_600
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.775333
common_nodes: [CreateCFGScheduleFloatList, HuMoEmbeds, INTConstant, ImageBatchMulti, ImageResizeKJv2, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, WhisperModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/1957726679996399618.json, 视频生成/文生视频/1968180863945027585.json, 视频生成/文生视频/humo双图参考_2072999565739204608.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_600

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1957726679996399618.json、视频生成/文生视频/1968180863945027585.json、视频生成/文生视频/humo双图参考_2072999565739204608.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `HuMoEmbeds`
- `INTConstant`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `NormalizeAudioLoudness`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WhisperModelLoader`

**可变部分**（部分 workflow 才有）：
- `SetNode` —— 2/3 个有
- `AudioToFPS` —— 1/3 个有
- `IndexTTS2Run` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `PreviewAudio` —— 1/3 个有
- `PrimitiveString` —— 1/3 个有
- `SaveAudio` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `ttN text` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
