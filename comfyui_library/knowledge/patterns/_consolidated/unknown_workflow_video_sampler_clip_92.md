---
name: unknown_workflow_video_sampler_clip_92
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.932286
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1_FusionX+lightx2v极速高质量首尾帧_1935617476765863938.json, 视频生成/图生视频/wan2.1美女跳舞比爱心_1945141161579225090.json, 视频生成/图生视频/wan2.1美女跳舞细节精准把控_1943857684569292801.json, 视频生成/图生视频/升级款刀切玻璃水果图生视频（可直播）_1940589072328929281.json, 视频生成/图生视频/电商商品展示图生视频_1923299741252112385.json, 视频生成/图生视频/直播切玻璃_1939900014733004802.json, 视频生成/图生视频/🦖Wan首尾帧视频_1905876278627733505.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_92

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Wan2.1_FusionX+lightx2v极速高质量首尾帧_1935617476765863938.json、视频生成/图生视频/wan2.1美女跳舞比爱心_1945141161579225090.json、视频生成/图生视频/wan2.1美女跳舞细节精准把控_1943857684569292801.json、视频生成/图生视频/升级款刀切玻璃水果图生视频（可直播）_1940589072328929281.json、视频生成/图生视频/电商商品展示图生视频_1923299741252112385.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 6/7 个有
- `WanVideoTeaCache` —— 6/7 个有
- `WanVideoImageClipEncode` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `Text` —— 3/7 个有
- `WanVideoClipVisionEncode` —— 2/7 个有
- `WanVideoImageToVideoEncode` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `ImageResize+` —— 1/7 个有
- `ImageResizeKJ` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `ResizeLongestToNode` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `easy int` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
