---
name: unknown_workflow_video_sampler_clip_46
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.981667
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/一刀两断特效，切开万物_1899035898183372801.json, 视频生成/图生视频/万象图生视频_1895446243693232129.json, 视频生成/图生视频/全平台网红跳舞视频_1994266529971765249.json, 视频生成/图生视频/图生视频  吻屏_1927610998885081089.json, 视频生成/图生视频/接吻一镜到底丝滑舌吻_1926200490214780930.json, 视频生成/图生视频/泼水变装_1932016531797159938.json, "视频生成/文生视频/泼水变装,动画迁移_1950803002250698754.json", "视频生成/文生视频/泼水变装,动画迁移_1951208338203848706.json", 视频生成/文生视频/泼水变装_1960218004153905154.json, 视频生成/文生视频/泼水变装性感红色花纹蕾丝内衣_1942781187436032002.json, 视频生成/文生视频/泼水变装红色内衣_1943248788255629314.json, 视频生成/文生视频/泼水变装红色内衣_1943678559179378689.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_46

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/一刀两断特效，切开万物_1899035898183372801.json、视频生成/图生视频/万象图生视频_1895446243693232129.json、视频生成/图生视频/全平台网红跳舞视频_1994266529971765249.json、视频生成/图生视频/图生视频  吻屏_1927610998885081089.json、视频生成/图生视频/接吻一镜到底丝滑舌吻_1926200490214780930.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 12 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 11/12 个有
- `easy imageSize` —— 11/12 个有
- `ImageScaleToTotalPixels` —— 10/12 个有
- `WanVideoTeaCache` —— 9/12 个有
- `RH_Captioner` —— 8/12 个有
- `easy cleanGpuUsed` —— 8/12 个有
- `LayerUtility: PurgeVRAM V2` —— 7/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/12 个有
- `Replace Text _O` —— 2/12 个有
- `TextInput_` —— 2/12 个有
- `Int` —— 1/12 个有
- `ShowText|pysssss` —— 1/12 个有
- `easy promptConcat` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
