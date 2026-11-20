---
name: unknown_workflow_video_sampler_vae_116
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8974
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/DeepSeek优化提示词+Wan文生视频_1900894135266459649.json, 视频生成/文生视频/Wan2.1文生视频【快速出片】_1911285182320836610.json, 视频生成/文生视频/【Wan2.1系列】文生视频工作流_1912089275754840066.json, 视频生成/文生视频/万相2.1-最强TEACACHE加速文生视频_1896798739846037506.json, 视频生成/文生视频/文生视频+通义万相KJ=艾橘溪_1895119782863831041.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_116

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/DeepSeek优化提示词+Wan文生视频_1900894135266459649.json、视频生成/文生视频/Wan2.1文生视频【快速出片】_1911285182320836610.json、视频生成/文生视频/【Wan2.1系列】文生视频工作流_1912089275754840066.json、视频生成/文生视频/万相2.1-最强TEACACHE加速文生视频_1896798739846037506.json、视频生成/文生视频/文生视频+通义万相KJ=艾橘溪_1895119782863831041.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoBlockSwap` —— 4/5 个有
- `WanVideoTeaCache` —— 4/5 个有
- `LayerUtility: PurgeVRAM` —— 3/5 个有
- `JjkText` —— 2/5 个有
- `LayerUtility: DeepSeekAPI` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `WanVideoEnhanceAVideo` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
