---
name: unknown_workflow_video_sampler_clip_41
type: Unknown Workflow
frequency: 12
level: weak
coverage: 0.9805
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/Smooth Mix 2.0 混合 LightX2V T2V_2073240392568492034.json, 视频生成/文生视频/Wan2.2_文生视频_4步极速版_ComfyUI官方流_2017117561548185601.json, 视频生成/文生视频/Wan2.2_文生视频_4步极速版_ComfyUI官方流_2044033029278011394.json, 视频生成/文生视频/Wan2.2文生视频_1985711544086474753.json, 视频生成/文生视频/Wan2.2文生视频_1997925759635324929.json, 视频生成/文生视频/Wan2.2文生视频_2007645581098881026.json, 视频生成/文生视频/1963477743868547073.json, 视频生成/文生视频/Wan2.2文生视频（优化版）_2067195635350196225.json, 视频生成/文生视频/1952262518809022466.json, 视频生成/文生视频/1950156709198217218.json, 视频生成/文生视频/1955111888410460162.json, 音频生成/音频生成/极速10s视频6步超极速图生视频V3只需3分钟_2046504111113248770.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_41

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/文生视频/Smooth Mix 2.0 混合 LightX2V T2V_2073240392568492034.json、视频生成/文生视频/Wan2.2_文生视频_4步极速版_ComfyUI官方流_2017117561548185601.json、视频生成/文生视频/Wan2.2_文生视频_4步极速版_ComfyUI官方流_2044033029278011394.json、视频生成/文生视频/Wan2.2文生视频_1985711544086474753.json、视频生成/文生视频/Wan2.2文生视频_1997925759635324929.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 9/12 个有
- `EmptyHunyuanLatentVideo` —— 8/12 个有
- `LoraLoaderModelOnly` —— 7/12 个有
- `JWInteger` —— 4/12 个有
- `LayerUtility: PurgeVRAM` —— 4/12 个有
- `WanImageToVideo` —— 4/12 个有
- `LoadImage` —— 3/12 个有
- `CR Prompt Text` —— 1/12 个有
- `LoraLoader` —— 1/12 个有
- `WujiAudioLoader` —— 1/12 个有
- `easy seed` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 12 | 50% |
| Prompt 约束强度(CFG) | 11 | 6 - 20 | 12 | 48% |
| 采样算法 | 1 | 1 - 3.5 | 12 | 40% |
| 调度器 | euler | - | 12 | 67% |
| 重绘幅度 | simple | - | 12 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，12 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 11，观测区间 6 - 20，12 个样本，取值分散，一致性仅 48%
- 采样算法 中位数 1，观测区间 1 - 3.5，12 个样本，取值分散，一致性仅 40%
- 调度器 最常用 euler，12 个样本，一致性 67%
- 重绘幅度 最常用 simple，12 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
