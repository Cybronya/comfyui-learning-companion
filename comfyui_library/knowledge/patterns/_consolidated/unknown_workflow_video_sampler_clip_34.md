---
name: unknown_workflow_video_sampler_clip_34
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.927923
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2016158718987079682.json, 视频生成/图生视频/1899415401065828354.json, 视频生成/图生视频/1900846163619389442.json, 视频生成/图生视频/1900090091270987777.json, 视频生成/图生视频/2034129372994605057.json, 视频生成/图生视频/1900825368478261250.json, 视频生成/图生视频/1899003016236941314.json, 视频生成/图生视频/1900079206938587137.json, 视频生成/图生视频/1899792108687863809.json, 视频生成/图生视频/1899801104287150081.json, 视频生成/图生视频/1899436993728696322.json, 视频生成/图生视频/1894738389084602370.json, 视频生成/文生视频/1894616411644538881.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_34

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/2016158718987079682.json、视频生成/图生视频/1899415401065828354.json、视频生成/图生视频/1900846163619389442.json、视频生成/图生视频/1900090091270987777.json、视频生成/图生视频/2034129372994605057.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 13 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadWanVideoT5TextEncoder` —— 12/13 个有
- `WanVideoBlockSwap` —— 12/13 个有
- `WanVideoTextEncode` —— 12/13 个有
- `WanVideoLoraSelect` —— 11/13 个有
- `Int` —— 5/13 个有
- `LayerUtility: PurgeVRAM` —— 5/13 个有
- `TextInput_` —— 4/13 个有
- `easy cleanGpuUsed` —— 2/13 个有
- `RH_Captioner` —— 1/13 个有
- `SaveAnimatedWEBP` —— 1/13 个有
- `WanVideoSetBlockSwap` —— 1/13 个有
- `WanVideoTeaCache` —— 1/13 个有
- `WanVideoTextEncodeCached` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
