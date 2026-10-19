---
name: unknown_workflow_video_lora_sampler_44
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.90681
common_nodes: [Int, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1924496227268743169.json, 视频生成/图生视频/1900145552707809282.json, 视频生成/图生视频/1931328744601137153.json, 视频生成/图生视频/2035705926753193985.json, 视频生成/图生视频/1924271202037059586.json, 视频生成/图生视频/1930223716829970433.json, 视频生成/图生视频/1956253952461426689.json, 视频生成/图生视频/1996610177388388353.json, 视频生成/图生视频/2065267287250259969.json, 视频生成/图生视频/1953668981687287809.json, 视频生成/图生视频/1976135458428162050.json, 视频生成/图生视频/2006375007433269250.json, 视频生成/图生视频/1976842256592392193.json, 视频生成/图生视频/1977972192019447810.json, 视频生成/图生视频/1978305034586873857.json, 视频生成/图生视频/2018188936127975425.json, 视频生成/图生视频/2068686422604861441.json, 视频生成/文生视频/1951219952894324738.json, 视频生成/文生视频/1950029325979533313.json, 视频生成/文生视频/泼水变装+换装_1991050908614205442.json, 视频生成/文生视频/1944994913614483458.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_44

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/图生视频/1924496227268743169.json、视频生成/图生视频/1900145552707809282.json、视频生成/图生视频/1931328744601137153.json、视频生成/图生视频/2035705926753193985.json、视频生成/图生视频/1924271202037059586.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 21 个 workflow 都包含：
- `Int`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 20/21 个有
- `easy cleanGpuUsed` —— 19/21 个有
- `MathExpression|pysssss` —— 18/21 个有
- `LayerUtility: PurgeVRAM` —— 14/21 个有
- `WanVideoClipVisionEncode` —— 14/21 个有
- `WanVideoImageToVideoEncode` —— 14/21 个有
- `WanVideoImageClipEncode` —— 7/21 个有
- `ImageSizeAndBatchSize` —— 4/21 个有
- `Fast Bypasser (rgthree)` —— 2/21 个有
- `Fast Groups Muter (rgthree)` —— 2/21 个有
- `Seed Everywhere` —— 2/21 个有
- `StringConstantMultiline` —— 2/21 个有
- `ImageScale` —— 1/21 个有
- `RIFE VFI` —— 1/21 个有
- `ReActorFaceSwapOpt` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
