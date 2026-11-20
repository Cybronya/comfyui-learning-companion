---
name: unknown_workflow_controlnet_video_lora_34
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9565
common_nodes: [Audio Duration (mtb), CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJ, ImageResizeKJv2, IndexTTS2Run, Int, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MaxNode, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PrimitiveStringMultiline, SaveAudio, VHS_LoadAudioUpload, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy anythingIndexSwitch, easy cleanGpuUsed]
problems: []
missing: []
members: [数字人/数字人/图生数字人、动物、MultiTalk + IndexTTS2语音克隆_2004539486237327361.json, 视频生成/图生视频/图生数字人、动物、角色--MultiTalk+IndexTTS2语音克隆_1936336489322041346.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_34

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/图生数字人、动物、MultiTalk + IndexTTS2语音克隆_2004539486237327361.json、视频生成/图生视频/图生数字人、动物、角色--MultiTalk+IndexTTS2语音克隆_1936336489322041346.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `Audio Duration (mtb)`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJ`
- `ImageResizeKJv2`
- `IndexTTS2Run`
- `Int`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MaxNode`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PrimitiveStringMultiline`
- `SaveAudio`
- `VHS_LoadAudioUpload`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `easy anythingIndexSwitch`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `WanVideoTeaCache` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
