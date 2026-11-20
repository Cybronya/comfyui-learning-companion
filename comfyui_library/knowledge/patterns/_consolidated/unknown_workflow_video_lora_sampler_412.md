---
name: unknown_workflow_video_lora_sampler_412
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.879143
common_nodes: [ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/利用图片替换视频中的角色_1916038900895121410.json, 图片生成/文生图/wan2.1 高速飘移动态特效_1936223818082062337.json, 平台全量/UniAnimate（姿态→视频）+WanVideo-720P_1914694029660094466.json, 平台全量/unianimate动画_1913579274467536898.json, 平台全量/人物和背景一致性舞蹈视频(UniAnimate)_1913611128453431298.json, 平台全量/图片动作控制 跳舞视频_1916096114783617026.json, 视频生成/图生视频/wan姿态控制图生视频_1914987342183002113.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_412

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/利用图片替换视频中的角色_1916038900895121410.json、图片生成/文生图/wan2.1 高速飘移动态特效_1936223818082062337.json、平台全量/UniAnimate（姿态→视频）+WanVideo-720P_1914694029660094466.json、平台全量/unianimate动画_1913579274467536898.json、平台全量/人物和背景一致性舞蹈视频(UniAnimate)_1913611128453431298.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `VHS_LoadVideo` —— 6/7 个有
- `WanVideoSLG` —— 6/7 个有
- `WanVideoUniAnimateDWPoseDetector` —— 6/7 个有
- `WanVideoUniAnimatePoseInput` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 5/7 个有
- `CLIPVisionLoader` —— 4/7 个有
- `LoadWanVideoClipTextEncoder` —— 3/7 个有
- `WanVideoExperimentalArgs` —— 3/7 个有
- `easy showAnything` —— 3/7 个有
- `GetNode` —— 2/7 个有
- `ImageConcanate` —— 2/7 个有
- `KepStringLiteral` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `Primitive integer [Crystools]` —— 2/7 个有
- `SetNode` —— 2/7 个有
- `easy clearCacheAll` —— 2/7 个有
- `DWPreprocessor` —— 1/7 个有
- `EmptyImage` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `ImageConcatMulti` —— 1/7 个有
- `MyOpenPoseNode` —— 1/7 个有
- `OpenposePreprocessor` —— 1/7 个有
- `Text Multiline` —— 1/7 个有
- `WanVideoVACEModelSelect` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
