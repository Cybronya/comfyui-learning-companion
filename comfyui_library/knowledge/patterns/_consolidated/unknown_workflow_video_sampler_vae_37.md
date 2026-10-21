---
name: unknown_workflow_video_sampler_vae_37
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.876364
common_nodes: [INTConstant, ImagePadKJ, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2017128536502439937.json, 视频生成/图生视频/2027315533716131841.json, 视频生成/图生视频/1933786059002007553.json, 视频生成/图生视频/1917399608392089601.json, 视频生成/图生视频/2019240301956702210.json, 视频生成/图生视频/1927581509937422337.json, 视频生成/图生视频/1971606625880567810.json, 视频生成/图生视频/1928697815218950145.json, 视频生成/图生视频/1935045733223735298.json, 视频生成/图生视频/1930083460306649089.json, 视频生成/文生视频/1937481435781447681.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_37

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/2017128536502439937.json、视频生成/图生视频/2027315533716131841.json、视频生成/图生视频/1933786059002007553.json、视频生成/图生视频/1917399608392089601.json、视频生成/图生视频/2019240301956702210.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
- `INTConstant`
- `ImagePadKJ`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoPhantomEmbeds`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 10/11 个有
- `WanVideoTextEncode` —— 9/11 个有
- `ImageConcatMulti` —— 8/11 个有
- `WanVideoTorchCompileSettings` —— 8/11 个有
- `WanVideoTeaCache` —— 7/11 个有
- `easy imageRemBg` —— 6/11 个有
- `Fast Groups Bypasser (rgthree)` —— 2/11 个有
- `FlashVSRNode` —— 2/11 个有
- `WanVideoApplyNAG` —— 2/11 个有
- `WanVideoTextEncodeSingle` —— 2/11 个有
- `Evaluate Integers` —— 1/11 个有
- `JjkText` —— 1/11 个有
- `Text _O` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
