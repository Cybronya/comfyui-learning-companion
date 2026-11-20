---
name: unknown_workflow_sampler_clip_vae_4
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.973667
common_nodes: [CLIPLoader, CLIPTextEncode, Fast Bypasser (rgthree), ImpactInt, KSamplerAdvanced, ModelPatchTorchSettings, ModelSamplingSD3, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, PrimitiveStringMultiline, Seed (rgthree), SimpleMath+, VAEDecode, VAELoader, WanImageToVideo, wanBlockSwap]
problems: []
missing: []
members: [图片生成/反推提示词/24ttovfast_2049408859428626433.json, 视频生成/图生视频/文生视频Wan2.2-Smooth+Mix++RTX超分+Qwen3.5_2053671434622386177.json, 视频生成/文生视频/Wan2.2 SmoothMix V3.0高动态电影质感 文生视频+补帧_2036248908665462786.json, 视频生成/文生视频/Wan2.2 Smoothmix全自动提示词4步加速渲染工作流_2043337939740004354.json, 视频生成/文生视频/wan2.2 SmoothMix V3.0高动态电影质感 文生视频+补帧_2041684980501323777.json, 视频生成/文生视频/wan2.2文生视频_2005367694092365826.json, 视频生成/文生视频/文生视频Wan2.2 GGUF 4步采样生成1k视频_2050852999907557378.json, 视频生成/文生视频/文生视频Wan2.2-Smooth Mix +RTX超分+Qwen3.5自动提示词+补帧动态电影感极速渲染_2038233332701470721.json, 视频生成/文生视频/文生视频Wan2.2-Smooth Mix +RTX超分+Qwen3.5自动提示词+补帧动态电影感极速渲染_2045817559047475201.json, 视频生成/文生视频/文生视频Wan2.2-Smooth Mix 超丝滑动态电影感画质极速渲染 工作流_1981303771013742594.json, 视频生成/文生视频/文生视频Wan2.2-Smooth Mix_2051648863991279617.json, 视频生成/文生视频/文生视频_2008897153195839489.json, 视频生成/文生视频/文生视频_2011579787898261505.json, 视频生成/文生视频/极速渲染优化！Wan2.2 SmoothMix+RTX+Qwen3.5提示词优化_2048029118243020801.json, 视频生成/文生视频/🌈老许Gary：文生视频Wan2.2-Smooth Mix_2045834738073604098.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_4

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/反推提示词/24ttovfast_2049408859428626433.json、视频生成/图生视频/文生视频Wan2.2-Smooth+Mix++RTX超分+Qwen3.5_2053671434622386177.json、视频生成/文生视频/Wan2.2 SmoothMix V3.0高动态电影质感 文生视频+补帧_2036248908665462786.json、视频生成/文生视频/Wan2.2 Smoothmix全自动提示词4步加速渲染工作流_2043337939740004354.json、视频生成/文生视频/wan2.2 SmoothMix V3.0高动态电影质感 文生视频+补帧_2041684980501323777.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Fast Bypasser (rgthree)`
- `ImpactInt`
- `KSamplerAdvanced`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `Seed (rgthree)`
- `SimpleMath+`
- `VAEDecode`
- `VAELoader`
- `WanImageToVideo`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 14/15 个有
- `UNETLoader` —— 14/15 个有
- `VHS_VideoCombine` —— 14/15 个有
- `RIFE VFI` —— 13/15 个有
- `LoraLoaderModelOnly` —— 9/15 个有
- `RTXVideoSuperResolution` —— 9/15 个有
- `ShowText` —— 7/15 个有
- `llama_cpp_instruct_adv` —— 7/15 个有
- `llama_cpp_model_loader` —— 7/15 个有
- `easy cleanGpuUsed` —— 6/15 个有
- `Wan22PromptSelector` —— 2/15 个有
- `easy promptConcat` —— 2/15 个有
- `CreateVideo` —— 1/15 个有
- `Int` —— 1/15 个有
- `SaveImage` —— 1/15 个有
- `SaveVideo` —— 1/15 个有
- `UnetLoaderGGUF` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 15 | 73% |
| Prompt 约束强度(CFG) | 6 | 4 - 8 | 15 | 78% |
| 采样算法 | 1 | 1 - 1 | 15 | 100% |
| 调度器 | euler_ancestral | - | 15 | 100% |
| 重绘幅度 | simple | - | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，15 个样本，一致性 73%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 8，15 个样本
- 采样算法 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，15 个样本，一致性 100%
- 重绘幅度 最常用 simple，15 个样本，一致性 100%
