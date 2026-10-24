---
name: unknown_workflow_video_lora_sampler_821
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.79
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, Fast Groups Bypasser (rgthree), INTConstant, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, VAEDecode, VHS_VideoCombine, WanVaceToVideo, WanVideoVACEStartToEndFrame, easy clearCacheAll, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Work-Fisher  -  全新AIO-MAGE-长视频_1968320251140157442.json, 视频生成/图生视频/iyuandou补充人脸素材工作流_1984201838234845185.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_821

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Work-Fisher  -  全新AIO-MAGE-长视频_1968320251140157442.json、视频生成/图生视频/iyuandou补充人脸素材工作流_1984201838234845185.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`
- `easy clearCacheAll`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `ImageBatch` —— 1/2 个有
- `ImageColorMatch+` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `StringLength` —— 1/2 个有
- `TorchCompileModelWanVideoV2` —— 1/2 个有
- `VHS_LoadVideoPath` —— 1/2 个有
- `VHS_PruneOutputs` —— 1/2 个有
- `VHS_SelectFilename` —— 1/2 个有
- `VHS_SplitImages` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | ipndm | - | 2 | 50% |
| 调度器 | sgm_uniform | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ipndm，2 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
