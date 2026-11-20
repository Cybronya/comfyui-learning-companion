---
name: unknown_workflow_video_lora_sampler_593
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.67875
common_nodes: [GetImageSizeAndCount, GetNode, ImageResizeKJ, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/万象VACE 14B视频扩展-加速版_1923359866998411265.json, 视频生成/图生视频/万象VACE 14B视频驱动图片-加速版_1923351461173129217.json, 视频生成/图生视频/万象加速时代-ACCVID_1927701391375253506.json, 视频生成/图生视频/（自用）Aniwan+百变星君（原59美元LORA）丝滑变装首尾帧_1952583718227652610.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_593

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/万象VACE 14B视频扩展-加速版_1923359866998411265.json、视频生成/图生视频/万象VACE 14B视频驱动图片-加速版_1923351461173129217.json、视频生成/图生视频/万象加速时代-ACCVID_1927701391375253506.json、视频生成/图生视频/（自用）Aniwan+百变星君（原59美元LORA）丝滑变装首尾帧_1952583718227652610.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 4 个 workflow 都包含：
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJ`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `AIO_Preprocessor` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `MaskPreview+` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `WanVideoTeaCache` —— 2/4 个有
- `GetImageRangeFromBatch` —— 1/4 个有
- `ImageBlend` —— 1/4 个有
- `ImagePadKJ` —— 1/4 个有
- `JWInteger` —— 1/4 个有
- `LoadLatent` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `SaveLatent` —— 1/4 个有
- `WanVideoVACEStartToEndFrame` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
