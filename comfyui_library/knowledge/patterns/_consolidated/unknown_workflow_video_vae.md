---
name: unknown_workflow_video_vae
type: Unknown Workflow
frequency: 33
level: moderate
coverage: 0.753303
common_nodes: [Audio Duration (mtb), AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1985223003455823873.json, 视频生成/图生视频/InfiniTetalk  数字人  口播对口型 情感口播   超自然数字人对口型_2085049062558097410.json, 视频生成/图生视频/2075937948620644353.json, 视频生成/图生视频/2080536331532455937.json, 视频生成/图生视频/1998620412286238722.json, 视频生成/图生视频/InfiniTetalk 对口型  超自然数字人情感口播 数字人_2082828282084548609.json, 视频生成/图生视频/InfiniTetalk 对口型 情感口播  数字人 超自然数字人对口型_2091473947605946369.json, 视频生成/图生视频/InfiniTetalk 对口型 情感口播  数字人 超自然数字人对口型_2091507985901244418.json, 视频生成/图生视频/2076605840307609602.json, 视频生成/图生视频/1998594240059990018.json, 视频生成/图生视频/InfiniTetalk 音频驱动+数字人电商带货_2096142991256801282.json, 视频生成/图生视频/InfiniTetalk+美化lora数字人workflow_2101551649981554690.json, 视频生成/图生视频/2046158426501287938.json, 视频生成/图生视频/2079894310165766146.json, 视频生成/图生视频/2080989129587908609.json, 视频生成/图生视频/2066129601021169666.json, 视频生成/图生视频/2082091396546252802.json, 视频生成/图生视频/2058786712498823169.json, 视频生成/图生视频/2043703040162668545.json, 视频生成/图生视频/2013593490084597762.json, 视频生成/图生视频/2039942750560325634.json, 视频生成/图生视频/2015642487410401281.json, 视频生成/图生视频/2058430451295019009.json, 视频生成/图生视频/2019698233995436034.json, 视频生成/图生视频/2040690138828771330.json, 视频生成/图生视频/2055645162226896897.json, 视频生成/图生视频/2026471529856372738.json, 视频生成/图生视频/2057657277599010818.json, 视频生成/图生视频/2020864511145676802.json, 视频生成/图生视频/2006359490202963970.json, 视频生成/图生视频/2053305138537873409.json, 视频生成/图生视频/2052944892057407490.json, 视频生成/图生视频/2033009151844032514.json]
source: knowledge_consolidation
---

# unknown_workflow_video_vae

> 由 `engine/knowledge_consolidation` 从 33 个 workflow 归纳得出（视频生成/图生视频/1985223003455823873.json、视频生成/图生视频/InfiniTetalk  数字人  口播对口型 情感口播   超自然数字人对口型_2085049062558097410.json、视频生成/图生视频/2075937948620644353.json、视频生成/图生视频/2080536331532455937.json、视频生成/图生视频/1998620412286238722.json…）

- **类型**：Unknown Workflow
- **样本数**：33
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 33 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoSampler` —— 32/33 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 31/33 个有
- `GetImageRangeFromBatch` —— 30/33 个有
- `GetNode` —— 30/33 个有
- `SetNode` —— 30/33 个有
- `WanVideoLoraSelect` —— 30/33 个有
- `PlaySound|pysssss` —— 29/33 个有
- `easy showAnything` —— 22/33 个有
- `easy int` —— 19/33 个有
- `Anything Everywhere` —— 18/33 个有
- `PreviewAudio` —— 17/33 个有
- `WanVideoTorchCompileSettings` —— 15/33 个有
- `ImageCASharpening+` —— 11/33 个有
- `ColorCorrectOfUtils` —— 10/33 个有
- `LayerMask: MaskPreview` —— 5/33 个有
- `SeparateMasks` —— 5/33 个有
- `Getter` —— 4/33 个有
- `Setter` —— 4/33 个有
- `LayerUtility: PurgeVRAM V2` —— 3/33 个有
- `WanVideoLoraSelectMulti` —— 3/33 个有
- `ImageResizeKJv2` —— 2/33 个有
- `QZ_ResolutionPreset` —— 2/33 个有
- `CR Text` —— 1/33 个有
- `PrimitiveInt` —— 1/33 个有
- `RHHiddenNodes` —— 1/33 个有
- `Text Multiline (Code Compatible)` —— 1/33 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
