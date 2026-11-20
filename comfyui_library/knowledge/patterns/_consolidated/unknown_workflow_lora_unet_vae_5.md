---
name: unknown_workflow_lora_unet_vae_5
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.950818
common_nodes: [CLIPLoader, CreateVideo, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/202610-minimax-h3-导演台-V2.0_2109257515652444161.json, 视频生成/图生视频/H3 导演台-R2V参考主体生视频_2089168093019987970.json, 视频生成/图生视频/MiniMax-导演台全能工作流_2086789063905988610.json, 视频生成/图生视频/Minimax-多参考长视频生成（导演台长视频）_2088245444265734145.json, 视频生成/图生视频/minimax导演台工作流_2090286084860235778.json, 视频生成/图生视频/minimax导演台工作流_2091395255663939586.json, 视频生成/文生视频/MINIMAX-H3导演台工作流_2092196369317580801.json, 视频生成/文生视频/MiniMax H3 Director 全能导演台_2093465779391000578.json, 视频生成/文生视频/Minimax-文生长视频生成（导演台长视频）_2087530746138423297.json, 视频生成/文生视频/minimax导演台工作流_2079449672288129026.json, 视频生成/文生视频/【开源】Minimax_H3 导演台参考生长视频_2089264892179206146.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_unet_vae_5

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/202610-minimax-h3-导演台-V2.0_2109257515652444161.json、视频生成/图生视频/H3 导演台-R2V参考主体生视频_2089168093019987970.json、视频生成/图生视频/MiniMax-导演台全能工作流_2086789063905988610.json、视频生成/图生视频/Minimax-多参考长视频生成（导演台长视频）_2088245444265734145.json、视频生成/图生视频/minimax导演台工作流_2090286084860235778.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CreateVideo`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 10/11 个有
- `MiniMaxH3Director` —— 7/11 个有
- `PathchSageAttentionKJ` —— 6/11 个有
- `ComfyMiniMaxH3Director` —— 4/11 个有
- `ModelAttentionBackend` —— 3/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `SolAttnMiniMax` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
