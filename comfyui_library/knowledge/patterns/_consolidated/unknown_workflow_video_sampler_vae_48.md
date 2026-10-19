---
name: unknown_workflow_video_sampler_vae_48
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.831778
common_nodes: [ImageResizeKJv2, JWInteger, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1933600414111551490.json, 视频生成/图生视频/1934292137033031682.json, 视频生成/图生视频/1937107842472005633.json, 视频生成/图生视频/1936024464108982273.json, 视频生成/图生视频/2018728714879635458.json, 视频生成/图生视频/2016926213708718081.json, 视频生成/图生视频/2017601924878573570.json, 视频生成/图生视频/1934575505217921026.json, 视频生成/图生视频/1933711937937002497.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_48

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1933600414111551490.json、视频生成/图生视频/1934292137033031682.json、视频生成/图生视频/1937107842472005633.json、视频生成/图生视频/1936024464108982273.json、视频生成/图生视频/2018728714879635458.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 9 个 workflow 都包含：
- `ImageResizeKJv2`
- `JWInteger`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoPhantomEmbeds`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 8/9 个有
- `ImageConcatMulti` —— 8/9 个有
- `VHS_Unbatch` —— 8/9 个有
- `AddLabel` —— 7/9 个有
- `EmptyImage` —— 7/9 个有
- `SetNode` —— 7/9 个有
- `WanVideoMagCache` —— 5/9 个有
- `WanVideoSLG` —— 5/9 个有
- `WanVideoTeaCache` —— 4/9 个有
- `CR Prompt Text` —— 1/9 个有
- `CR Text` —— 1/9 个有
- `SimpleMath+` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
