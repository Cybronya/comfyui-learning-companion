---
name: unknown_workflow_video_sampler_vae_111
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8806
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/1900894135266459649.json, 视频生成/文生视频/1911285182320836610.json, 视频生成/文生视频/1894655158603677697.json, 视频生成/文生视频/1896798739846037506.json, 视频生成/文生视频/1895119782863831041.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_111

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/1900894135266459649.json、视频生成/文生视频/1911285182320836610.json、视频生成/文生视频/1894655158603677697.json、视频生成/文生视频/1896798739846037506.json、视频生成/文生视频/1895119782863831041.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：88%

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
- `LayerUtility: PurgeVRAM` —— 3/5 个有
- `WanVideoTeaCache` —— 3/5 个有
- `JjkText` —— 2/5 个有
- `LayerUtility: DeepSeekAPI` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `WanVideoTorchCompileSettings` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
