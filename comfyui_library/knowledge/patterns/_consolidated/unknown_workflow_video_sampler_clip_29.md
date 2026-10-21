---
name: unknown_workflow_video_sampler_clip_29
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.951357
common_nodes: [CLIPLoader, CLIPTextEncode, Fast Bypasser (rgthree), ImageScaleBy, ImpactInt, KSamplerAdvanced, ModelPatchTorchSettings, ModelSamplingSD3, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, PrimitiveStringMultiline, Seed (rgthree), SimpleMath+, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, wanBlockSwap]
problems: []
missing: [Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), Note Plus (mtb), RIFE VFI, SimpleMath+, easy cleanGpuUsed, Seed (rgthree)]
members: [视频生成/文生视频/1979382260715655170.json, 视频生成/文生视频/Wan2.2 SmoothMix V3.0高动态电影质感 文生视频+补帧_2036248908665462786.json, 视频生成/文生视频/Wan2.2 Smoothmix全自动提示词4步加速渲染工作流_2043337939740004354.json, 视频生成/文生视频/wan2.2 SmoothMix V3.0高动态电影质感 文生视频+补帧_2041684980501323777.json, 视频生成/文生视频/wan2.2文生视频_2005367694092365826.json, 视频生成/文生视频/文生视频Wan2.2 GGUF 4步采样生成1k视频_2050852999907557378.json, 视频生成/文生视频/文生视频Wan2.2-Smooth Mix +RTX超分+Qwen3.5自动提示词+补帧动态电影感极速渲染_2038233332701470721.json, 视频生成/文生视频/文生视频Wan2.2-Smooth Mix +RTX超分+Qwen3.5自动提示词+补帧动态电影感极速渲染_2045817559047475201.json, 视频生成/文生视频/文生视频Wan2.2-Smooth Mix 超丝滑动态电影感画质极速渲染 工作流_1981303771013742594.json, 视频生成/文生视频/文生视频Wan2.2-Smooth Mix_2051648863991279617.json, 视频生成/文生视频/文生视频_2008897153195839489.json, 视频生成/文生视频/文生视频_2011579787898261505.json, 视频生成/文生视频/极速渲染优化！Wan2.2 SmoothMix+RTX+Qwen3.5提示词优化_2048029118243020801.json, 视频生成/文生视频/🌈老许Gary：文生视频Wan2.2-Smooth Mix_2045834738073604098.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_29

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/文生视频/1979382260715655170.json、视频生成/文生视频/Wan2.2 SmoothMix V3.0高动态电影质感 文生视频+补帧_2036248908665462786.json、视频生成/文生视频/Wan2.2 Smoothmix全自动提示词4步加速渲染工作流_2043337939740004354.json、视频生成/文生视频/wan2.2 SmoothMix V3.0高动态电影质感 文生视频+补帧_2041684980501323777.json、视频生成/文生视频/wan2.2文生视频_2005367694092365826.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Fast Bypasser (rgthree)`
- `ImageScaleBy`
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
- `VHS_VideoCombine`
- `WanImageToVideo`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `RIFE VFI` —— 13/14 个有
- `UNETLoader` —— 13/14 个有
- `LoraLoaderModelOnly` —— 7/14 个有
- `RTXVideoSuperResolution` —— 7/14 个有
- `easy cleanGpuUsed` —— 7/14 个有
- `ShowText` —— 5/14 个有
- `llama_cpp_instruct_adv` —— 5/14 个有
- `llama_cpp_model_loader` —— 5/14 个有
- `Wan22PromptSelector` —— 2/14 个有
- `easy promptConcat` —— 2/14 个有
- `Note Plus (mtb)` —— 1/14 个有
- `SaveImage` —— 1/14 个有
- `UnetLoaderGGUF` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 14 | 64% |
| Prompt 约束强度(CFG) | 6 | 4 - 8 | 14 | 82% |
| 采样算法 | 1 | 1 - 1 | 14 | 100% |
| 调度器 | euler_ancestral | - | 14 | 100% |
| 重绘幅度 | simple | - | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，14 个样本，一致性 64%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 8，14 个样本，取值集中（一致性 82%）
- 采样算法 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，14 个样本，一致性 100%
- 重绘幅度 最常用 simple，14 个样本，一致性 100%
- 这些节点还没有知识卡，系统对它们的理解有限：Fast Bypasser (rgthree)、Mute / Bypass Repeater (rgthree)、Note Plus (mtb)、RIFE VFI、SimpleMath+
