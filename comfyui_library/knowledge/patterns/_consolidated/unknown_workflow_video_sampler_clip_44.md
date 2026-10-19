---
name: unknown_workflow_video_sampler_clip_44
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.879818
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1907807736166232066.json, 视频生成/图生视频/1895074790560956417.json, 视频生成/图生视频/1932067236700127234.json, 视频生成/图生视频/1914225072540741633.json, 视频生成/图生视频/1914706731866255362.json, 视频生成/图生视频/1926816500064358401.json, 视频生成/图生视频/1905280453560176642.json, 视频生成/图生视频/1903813340349501441.json, 视频生成/图生视频/1913242706372456449.json, 视频生成/图生视频/1911248941428736001.json, 视频生成/图生视频/1914494071358877697.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_44

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/1907807736166232066.json、视频生成/图生视频/1895074790560956417.json、视频生成/图生视频/1932067236700127234.json、视频生成/图生视频/1914225072540741633.json、视频生成/图生视频/1914706731866255362.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
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
- `WanVideoSLG` —— 10/11 个有
- `WanVideoTeaCache` —— 10/11 个有
- `WanVideoExperimentalArgs` —— 9/11 个有
- `JWInteger` —— 8/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/11 个有
- `LayerUtility: PurgeVRAM` —— 8/11 个有
- `WanVideoEnhanceAVideo` —— 8/11 个有
- `CR Prompt Text` —— 7/11 个有
- `Note Plus (mtb)` —— 3/11 个有
- `HyVideoEnhanceAVideo` —— 2/11 个有
- `LTXVPromptEnhancer` —— 2/11 个有
- `LTXVPromptEnhancerLoader` —— 2/11 个有
- `LoadLatent` —— 2/11 个有
- `SaveImage` —— 2/11 个有
- `SaveLatent` —— 2/11 个有
- `PrimitiveInt` —— 1/11 个有
- `String Literal` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
