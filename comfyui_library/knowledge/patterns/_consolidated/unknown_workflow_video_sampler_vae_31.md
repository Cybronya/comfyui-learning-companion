---
name: unknown_workflow_video_sampler_vae_31
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.973636
common_nodes: [CLIPVisionLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/AI数字人-动物_2084929827878031362.json, 视频生成/图生视频/1997484530254680066.json, 视频生成/图生视频/1987166609188040706.json, 视频生成/图生视频/2071856835908427777.json, 视频生成/图生视频/2072507975016738818.json, 视频生成/图生视频/2072619753109278721.json, 视频生成/图生视频/2074016139532918786.json, 视频生成/图生视频/2008048511492825090.json, 视频生成/图生视频/2073956730425401346.json, 视频生成/图生视频/1957839924697427969.json, 视频生成/图生视频/1957830385059164161.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_31

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/AI数字人-动物_2084929827878031362.json、视频生成/图生视频/1997484530254680066.json、视频生成/图生视频/1987166609188040706.json、视频生成/图生视频/2071856835908427777.json、视频生成/图生视频/2072507975016738818.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPVisionLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 10/11 个有
- `WanVideoLoraSelect` —— 10/11 个有
- `Audio Duration` —— 6/11 个有
- `ComfyMathExpression` —— 6/11 个有
- `Wav2VecModelLoader` —— 6/11 个有
- `AudioCrop` —— 5/11 个有
- `AudioSeparation` —— 5/11 个有
- `DownloadAndLoadWav2VecModel` —— 5/11 个有
- `LogicUtil_CeilNode` —— 4/11 个有
- `CR Prompt Text` —— 3/11 个有
- `JWInteger` —— 3/11 个有
- `SimpleMath+` —— 2/11 个有
- `INTConstant` —— 1/11 个有
- `Int` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `VHS_LoadVideo` —— 1/11 个有
- `WanVideoLoraSelectMulti` —— 1/11 个有
- `WanVideoTorchCompileSettings` —— 1/11 个有
- `easy showAnything` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
