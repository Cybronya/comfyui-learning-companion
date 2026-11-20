---
name: unknown_workflow_video_lora_sampler_217
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.892
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/AI 3D破屏特效~当企鹅🐧打破次元壁来到现实！_1996567889761148929.json, 视频生成/图生视频/AI 3D破屏特效~当企鹅🐧打破次元壁来到现实！_1997217286731796481.json, 视频生成/图生视频/AI 3D破屏特效~当企鹅🐧打破次元壁来到现实！（企鹅的越狱实录）_1996051204809637889.json, 视频生成/图生视频/Aiwood-magref+Lightx2v 4步lora双图参考_1935019141126660097.json, 视频生成/图生视频/Aiwood-magref+Lightx2v 4步lora双图参考_1935258795541200897.json, 视频生成/图生视频/Aiwood-magref+Lightx2v 4步lora双图参考_1935559387752615938.json, 视频生成/图生视频/Aiwood-magref三图参考_1935019116438691841.json, 视频生成/图生视频/Aiwood-magref三图参考_1935263109068292098.json, 视频生成/图生视频/Aiwood-magref三图参考_1935557538790440962.json, 视频生成/图生视频/BindWeave-图生视频-高人物一致性-单角色（推荐）_1988930227843764225.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_217

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/AI 3D破屏特效~当企鹅🐧打破次元壁来到现实！_1996567889761148929.json、视频生成/图生视频/AI 3D破屏特效~当企鹅🐧打破次元壁来到现实！_1997217286731796481.json、视频生成/图生视频/AI 3D破屏特效~当企鹅🐧打破次元壁来到现实！（企鹅的越狱实录）_1996051204809637889.json、视频生成/图生视频/Aiwood-magref+Lightx2v 4步lora双图参考_1935019141126660097.json、视频生成/图生视频/Aiwood-magref+Lightx2v 4步lora双图参考_1935258795541200897.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 7/10 个有
- `easy imageRemBg` —— 7/10 个有
- `ImagePadKJ` —— 6/10 个有
- `Int` —— 4/10 个有
- `WanVideoSetBlockSwap` —— 4/10 个有
- `WanVideoTorchCompileSettings` —— 4/10 个有
- `DownloadAndLoadGIMMVFIModel` —— 3/10 个有
- `GIMMVFI_interpolate` —— 3/10 个有
- `GetImageSize+` —— 3/10 个有
- `RH_Jimeng4_Image2Image` —— 3/10 个有
- `Textbox` —— 3/10 个有
- `CR Text` —— 1/10 个有
- `InvertMask` —— 1/10 个有
- `MaskPreview+` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `Seed Generator` —— 1/10 个有
- `WanVideoAddBindweaveEmbeds` —— 1/10 个有
- `WanVideoEncodeLatentBatch` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
