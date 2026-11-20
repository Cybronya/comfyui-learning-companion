---
name: unknown_workflow_video_lora_sampler_326
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.73175
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoNAG]
problems: []
missing: []
members: [视频生成/文生视频/lora训练工具之五：wan2.2训练lora参数测试工作流（多模型综合加速文生视频）_1954421837595865089.json, 视频生成/文生视频/video_wan2_2_14B_Smooth Mix_1980199127709552641.json, 视频生成/文生视频/video_wan2_2_14B_holocine_1984147805432414210.json, 视频生成/文生视频/video_wan2_2_14B_qwenvl-prompt-generate_1981270580760576001.json, 视频生成/文生视频/video_wan2_2_14B_rewards_lora_1966051284912607234.json, 视频生成/文生视频/video_wan2_2_14B_t2v_优化版_1972464256455208962.json, 视频生成/文生视频/video_wan2_2_14B_多模精度型混用加速_1952546698105163778.json, 视频生成/文生视频/video_wan2_2_14B_多模精度型混用加速_1952688713274953729.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_326

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/lora训练工具之五：wan2.2训练lora参数测试工作流（多模型综合加速文生视频）_1954421837595865089.json、视频生成/文生视频/video_wan2_2_14B_Smooth Mix_1980199127709552641.json、视频生成/文生视频/video_wan2_2_14B_holocine_1984147805432414210.json、视频生成/文生视频/video_wan2_2_14B_qwenvl-prompt-generate_1981270580760576001.json、视频生成/文生视频/video_wan2_2_14B_rewards_lora_1966051284912607234.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `CFGZeroStar` —— 7/8 个有
- `PathchSageAttentionKJ` —— 7/8 个有
- `GetNode` —— 5/8 个有
- `SetNode` —— 5/8 个有
- `UnetLoaderGGUF` —— 3/8 个有
- `AILab_QwenVL` —— 2/8 个有
- `PreviewAny` —— 2/8 个有
- `HunyuanImageToVideo` —— 1/8 个有
- `ShellAgentPluginInputImage` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 62% |
| Prompt 约束强度(CFG) | 8 | 6 - 8 | 8 | 91% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | lcm | - | 8 | 88% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 62%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 8，8 个样本，取值集中（一致性 91%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，8 个样本，一致性 88%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
