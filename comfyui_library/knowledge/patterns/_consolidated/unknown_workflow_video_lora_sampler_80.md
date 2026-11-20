---
name: unknown_workflow_video_lora_sampler_80
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.84605
common_nodes: [CLIPLoader, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/Bernini studio自由切换提示词前缀_2064529633915269122.json, 平台全量/Wan2.2-Bernini-视频编辑人物替换_2061782097475489794.json, 平台全量/贝尔尼尼Bernini Studio工作流-4步lora加速-视频修改_2073757279970742274.json, 平台全量/贝尔尼尼Bernini Studio工作流_2063961104111460354.json, 视频生成/图生视频/Bernini Studio 参考图出视频_2078439441877790721.json, 视频生成/图生视频/Bernini Studio-图生视频（超级加速）_2073592310989942786.json, 视频生成/图生视频/Bernini Studio-视频编辑（超级加速）_2073584193665331202.json, 视频生成/图生视频/Bernini Studio图生视频工作流_2065400514141048833.json, 视频生成/图生视频/Bernini Studio多图参考工作流_2081577097444810753.json, 视频生成/图生视频/Bernini Studio贝尔尼尼_2075050205141094402.json, 视频生成/图生视频/Bernini-4步加速-图生视频_2074045202817437698.json, 视频生成/图生视频/多功能视频处理，图生视频  视频编辑 Bernini Studio 加速版_2063147705244930049.json, 视频生成/图生视频/视频编辑，图生视频 Bernini Studio 贝尔尼尼 急速版_2064931292038385665.json, 视频生成/图生视频/调试Bernini Studio工作流-4步lora_rv2v_2102665904747270146.json, 视频生成/图生视频/贝尔尼尼Bernini Studio工作流-4步lora-双参考图_2073745061728313345.json, 视频生成/图生视频/贝尔尼尼Bernini Studio工作流-4步lora_2073682935554854913.json, 视频生成/图生视频/贝尔尼尼Bernini Studio工作流-Remix-lora+4步lora加速_2082366639907102721.json, 视频生成/图生视频/贝尔尼尼Bernini Studio工作流-Remix-lora+4步lora加速_2082437380983844866.json, 视频生成/图生视频/贝尔尼尼Bernini Studio工作流-Remix-lora+4步lora加速_2082454463452893186.json, 视频生成/图生视频/贝尔尼尼Bernini Studio工作流-Remix-lora+4步lora加速_2082456967376883713.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_80

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/文生图/Bernini studio自由切换提示词前缀_2064529633915269122.json、平台全量/Wan2.2-Bernini-视频编辑人物替换_2061782097475489794.json、平台全量/贝尔尼尼Bernini Studio工作流-4步lora加速-视频修改_2073757279970742274.json、平台全量/贝尔尼尼Bernini Studio工作流_2063961104111460354.json、视频生成/图生视频/Bernini Studio 参考图出视频_2078439441877790721.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BerniniStudio` —— 19/20 个有
- `VHS_LoadVideo` —— 18/20 个有
- `GetNode` —— 17/20 个有
- `SetNode` —— 17/20 个有
- `RTXVideoSuperResolution` —— 16/20 个有
- `ImageConcatMulti` —— 15/20 个有
- `Int` —— 13/20 个有
- `SimpleMath+` —— 12/20 个有
- `ComfyNumberConvert` —— 3/20 个有
- `VHS_VideoInfo` —— 2/20 个有
- `BerniniConditioningReferenceSlots` —— 1/20 个有
- `CLIPTextEncode` —— 1/20 个有
- `Fast Groups Bypasser (rgthree)` —— 1/20 个有
- `ShowAnything|Mie` —— 1/20 个有
- `Text` —— 1/20 个有
- `easy showAnything` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 20 | 70% |
| Prompt 约束强度(CFG) | 4 | 4 - 8 | 20 | 77% |
| 采样算法 | 1 | 1 - 1 | 20 | 100% |
| 调度器 | euler | - | 20 | 95% |
| 重绘幅度 | simple | - | 20 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，20 个样本，一致性 70%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 8，20 个样本
- 采样算法 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，20 个样本，一致性 95%
- 重绘幅度 最常用 simple，20 个样本，一致性 100%
