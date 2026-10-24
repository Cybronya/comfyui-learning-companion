---
name: unknown_workflow_video_lora_sampler_278
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.851125
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/video_wan2_2_14B_rewards_lora_1966051284912607234.json, 视频生成/文生视频/video_wan2_2_14B_t2v_优化版_1972464256455208962.json, 视频生成/文生视频/video_wan2_2_14B_多模精度型混用加速_1952546698105163778.json, 视频生成/文生视频/video_wan2_2_14B_多模精度型混用加速_1952688713274953729.json, 视频生成/文生视频/video_wan2_2_14B_灯光工作流+提示词_1950503507558387713.json, 视频生成/文生视频/wan2.2+2.1文生视频_1950156709198217218.json, 视频生成/文生视频/wan2.2文生视频-官方极速版_1950456441427693570.json, 视频生成/文生视频/wan2_2_t2v-生万物+妙转换+广告创意动画-高质量_1973586939590873089.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_278

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/video_wan2_2_14B_rewards_lora_1966051284912607234.json、视频生成/文生视频/video_wan2_2_14B_t2v_优化版_1972464256455208962.json、视频生成/文生视频/video_wan2_2_14B_多模精度型混用加速_1952546698105163778.json、视频生成/文生视频/video_wan2_2_14B_多模精度型混用加速_1952688713274953729.json、视频生成/文生视频/video_wan2_2_14B_灯光工作流+提示词_1950503507558387713.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 7/8 个有
- `PathchSageAttentionKJ` —— 6/8 个有
- `WanVideoNAG` —— 6/8 个有
- `CFGZeroStar` —— 4/8 个有
- `UnetLoaderGGUF` —— 3/8 个有
- `GetNode` —— 2/8 个有
- `SetNode` —— 2/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `easy seed` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 50% |
| Prompt 约束强度(CFG) | 8 | 8 - 20 | 8 | 59% |
| 采样算法 | 1 | 1 - 3.5 | 8 | 37% |
| 调度器 | lcm | - | 8 | 62% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 20，8 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，8 个样本，取值分散，一致性仅 37%
- 调度器 最常用 lcm，8 个样本，一致性 62%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
